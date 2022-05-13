using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using System.Threading;
using System.Net.Sockets;
using System.Text;
using System.Net;
using System.Threading.Tasks;
using System.Security.Cryptography;
using System.IO;
using Thelara.MVVM.ViewModel;

namespace Thelara.MVVM.Model
{
    public class Network
    {
        protected static internal NetworkStream Stream { get; private set; }
        public static TcpListener tcpListener; // сервер для прослушивания
        public static string recivedMessage = null;
        public static Package actualPackage = null;
        public class Package
        {
            public string To { get; set; }
            public string From { get; set; }
            public string Data { get; set; }
            public byte[] seanceKey { get; set; }

        }
        public class SecretPackage
        {
            public string To { get; set; }
            public string From { get; set; }
            public byte[] SecretData { get; set; }
            public byte[] iv { get; set; }

        }

        public class Address
        {
            public string IPv4;
            public string Port;
        }

        public class Node
        {
            public Dictionary<string, bool> Connections;
            public Dictionary<string, byte[]> PublicKeys;
            public ECDiffieHellmanCng nodeKey { get; set; }
            public byte[] _PublicKey { get; set; }
            public Address address = new Address();
            public byte[] mixedKey { get; set; }
            public void ConnectTo(string addreses, Node node)
            {
                node.Connections.Add(addreses, true);

            }
            public void SendMessageToAll(Node node, string message)
            {
                Package new_pack = new Package();
                {
                    new_pack.From = node.address.IPv4 + ":" + node.address.Port;
                    new_pack.Data = message;
                }
                foreach (var addr in node.Connections)
                {
                    new_pack.To = addr.Key;
                    node.Send(new_pack, node);
                }
            }
            public void Send(Package package, Node node)
            {
                string[] splited = package.To.Split(':');

                TcpClient tcpClient = new TcpClient();
                try
                {
                    tcpClient.Connect(splited[0], Convert.ToInt32(splited[1]));
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                    node.Connections.Remove(package.To);
                }

                NetworkStream stream = tcpClient.GetStream();

                var json = JsonConvert.SerializeObject(package);

                byte[] data = Encoding.UTF8.GetBytes(json);
                stream.Write(data, 0, data.Length);
                tcpClient.Close();
            }
            public void HideSend(Node node, byte[] Key, SecretPackage package)
            {
                string[] splited = package.To.Split(':');
                byte[] encryptedMessage;
                TcpClient tcpClient = new TcpClient();
                try
                {
                    tcpClient.Connect(splited[0], Convert.ToInt32(splited[1]));
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                    node.Connections.Remove(package.To);
                }

                NetworkStream stream = tcpClient.GetStream();

                using (Aes aes = new AesCryptoServiceProvider())
                {
                    aes.Key = Key;
                    package.iv = aes.IV;

                    // Console.WriteLine(Encoding.UTF8.GetString(Key) + "      "+ Encoding.UTF8.GetString(aes.IV));
                    // Encrypt the message
                    using (MemoryStream ciphertext = new MemoryStream())
                    using (CryptoStream cs = new CryptoStream(ciphertext, aes.CreateEncryptor(), CryptoStreamMode.Write))
                    {
                        byte[] plaintextMessage = package.SecretData;
                        cs.Write(plaintextMessage, 0, plaintextMessage.Length);
                        cs.FlushFinalBlock();
                        cs.Close();
                        encryptedMessage = ciphertext.ToArray();
                    }

                }
                // Console.WriteLine("hey "+ encryptedMessage.Length+ "do " + Encoding.UTF8.GetString(encryptedMessage));
                package.SecretData = encryptedMessage;

                var json = JsonConvert.SerializeObject(package);
                byte[] data = Encoding.UTF8.GetBytes(json);

                stream.Write(data, 0, data.Length);
                tcpClient.Close();
            }
            public void SendToContact(Node node, string address, string message)
            {
                Package new_pack = new Package();
                {
                    new_pack.From = node.address.IPv4 + ":" + node.address.Port;
                    new_pack.Data = message;
                    new_pack.seanceKey = node._PublicKey;
                }

                new_pack.To = address;
                node.Send(new_pack, node);
            }
            public void ChiperSendTo(Node node, string address, string message)
            {
                var new_node = KeyReciverMixer(node.PublicKeys[address], node);

                var Key = new_node.mixedKey;
                SecretPackage new_pack = new SecretPackage();
                {
                    new_pack.From = node.address.IPv4 + ":" + node.address.Port;
                    new_pack.SecretData = Encoding.UTF8.GetBytes(message);
                }

                new_pack.To = address;
                node.HideSend(node, Key, new_pack);
            }

            public Node KeyMixer(byte[] publicKey, Node node)
            {
                var MixKey = node.nodeKey;

                node.mixedKey = MixKey.DeriveKeyMaterial(CngKey.Import(publicKey, CngKeyBlobFormat.EccPublicBlob));
                Console.WriteLine(Encoding.UTF8.GetString(node.mixedKey));
                return node;

            }
            public Node KeyReciverMixer(byte[] publicKey, Node node)    //ERR go lane 211
            {
                var MixKey = node.nodeKey;

                CngKey SenderKey = CngKey.Import(publicKey, CngKeyBlobFormat.EccPublicBlob);
                byte[] recivereKey = MixKey.DeriveKeyMaterial(SenderKey);
                node.mixedKey = recivereKey;
                //Console.WriteLine(Encoding.UTF8.GetString(node.mixedKey));
                return node;

            }
            public void PrintNetwork(Node node)
            {
                foreach (var addr in node.Connections)
                {
                    Console.WriteLine("| " + addr);
                }
            }
        }

        public static Node NewNode(string address)
        {
            Node node = new Node();

            string[] splited = address.Split(':');

            if (splited.Length != 2)
                return node;

            else
            {
                node.address.IPv4 = splited[0];
                node.address.Port = splited[1];
                node.Connections = new Dictionary<string, bool>();
                node.PublicKeys = new Dictionary<string, byte[]>();
            }

            node.nodeKey = new ECDiffieHellmanCng();
            node.nodeKey.KeyDerivationFunction = ECDiffieHellmanKeyDerivationFunction.Hash;
            node.nodeKey.HashAlgorithm = CngAlgorithm.Sha256;
            node._PublicKey = node.nodeKey.PublicKey.ToByteArray();

            return node;
        }
        public async static void Run(Node node)
        {
            Thread myThread = new Thread(() => handleClient(node));
            myThread.Start();
            await handelServer(node);
        }
        public static async Task handelServer(Node node)
        {
            try
            {
                tcpListener = new TcpListener(IPAddress.Any, Convert.ToInt32(node.address.Port));
                tcpListener.Start();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }

            while (true)
            {
                //TcpClient tcpClient = tcpListener.AcceptTcpClient();
                var tcpClient = await tcpListener.AcceptTcpClientAsync();
                /* await*/
                handleConnection(tcpClient, node);
                //if (handleConnection(tcpClient, node).Exception.Data != null)
                //    tcpListener.Stop();
            }

        }
        public static Task handleChipherConnection(SecretPackage deserializedWeatherForecast, Node node)
        {

            using (Aes aes = new AesCryptoServiceProvider())
            {
                if (node.mixedKey == null)
                    node = node.KeyMixer(node.PublicKeys[deserializedWeatherForecast.From], node);

                aes.Key = node.mixedKey;
                aes.IV = deserializedWeatherForecast.iv;
                aes.Padding = PaddingMode.None;

                // Console.WriteLine(Encoding.UTF8.GetString(node.mixedKey) + "      " + Encoding.UTF8.GetString(deserializedWeatherForecast.iv));
                // Decrypt the message
                // Console.WriteLine(deserializedWeatherForecast.SecretData);

                byte[] encryptedmsg = deserializedWeatherForecast.SecretData;

                using (MemoryStream plaintext = new MemoryStream())
                {
                    using (CryptoStream cs = new CryptoStream(plaintext, aes.CreateDecryptor(), CryptoStreamMode.Write))
                    {
                        cs.Write(encryptedmsg, 0, encryptedmsg.Length);
                        cs.Close();
                        string message = Encoding.UTF8.GetString(plaintext.ToArray());
                        Console.WriteLine(message);
                    }
                }
            }
            return Task.CompletedTask;

        }

        public static Task handleConnection(TcpClient tcpClient, Node node)
        {
            NetworkStream ns = tcpClient.GetStream();
            byte[] bytes = new byte[tcpClient.ReceiveBufferSize];
            do
            {
                ns.Read(bytes, 0, tcpClient.ReceiveBufferSize);
            }
            while (ns.DataAvailable);

            string jsonStr = Encoding.UTF8.GetString(bytes);

            if (jsonStr.Contains("seanceKey"))
            {
                Package deserializedWeatherForecast = JsonConvert.DeserializeObject<Package>(jsonStr);
                if (!node.Connections.ContainsKey(deserializedWeatherForecast.From))
                    node.ConnectTo(deserializedWeatherForecast.From, node);
                actualPackage = deserializedWeatherForecast;
                //Console.WriteLine("Пришло сообщение: " + deserializedWeatherForecast.Data + " от " + deserializedWeatherForecast.From);
                recivedMessage = deserializedWeatherForecast.Data;
                if (!node.PublicKeys.ContainsKey(deserializedWeatherForecast.From))
                    node.PublicKeys.Add(deserializedWeatherForecast.From, deserializedWeatherForecast.seanceKey);

                tcpClient.Close();
                return Task.CompletedTask;
            }
            else
            {
                SecretPackage deserializedWeatherForecast = JsonConvert.DeserializeObject<SecretPackage>(jsonStr);
                handleChipherConnection(deserializedWeatherForecast, node);
                return Task.CompletedTask;
            }
        }
        public static void handleClient(Node node)
        {
            string message;
            node.Connections.Add("127.0.0.1:8080", true);
            node.Connections.Add("127.0.0.1:8082", true);
            node.Connections.Add("127.0.0.1:8083", true);
            node.Connections.Add("127.0.0.1:8084", true);
            node.Connections.Add("127.0.0.1:8085", true);
            while (true)
            {
                //    Console.WriteLine("Введите /команду адресс и сообщение: ");
                //    message = Console.ReadLine();
                //    string[] splited = message.Split(" ");

                //    switch (splited[0])
                //    {
                //        case "/exit": return;
                //        case "/connect":
                //            node.ConnectTo(splited[1], node);
                //            break;
                //        case "/network":
                //            node.PrintNetwork(node);
                //            break;
                //        case "/sendto":
                //            node.SendToContact(node, splited[1], splited[2]);
                //            break;
                //        case "/chiper":
                //            node.ChiperSendTo(node, splited[1], splited[2]);
                //            break;
                //        default:
                //            node.SendMessageToAll(node, message);
                //            break;


                //    }
            }
        }
        //static void Main(string[] args)
        //{
        //    string addr;
        //    Console.WriteLine("Введите свой адресс в формате Address:port");
        //    addr = Console.ReadLine();
        //    var node = NewNode(addr);
        //    Run(node);
        //}
    }
}
