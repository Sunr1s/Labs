using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Net.Sockets;
using Newtonsoft.Json;

namespace Oodp_6
{
    public class ClientObject
    {
        public class Package
        {
            public string To { get; set; }
            public string From { get; set; }
            public string Data { get; set; }

        }
        protected internal string Id { get; private set; }
        protected internal NetworkStream Stream { get; private set; }
        string userName;
        TcpClient client;
        ServerObject server; // объект сервера


        public ClientObject(TcpClient tcpClient, ServerObject serverObject)
        {
            Id = Guid.NewGuid().ToString();
            client = tcpClient;
            server = serverObject;
            serverObject.AddConnection(this);
        }

        public void Process()
        {
            try
            {
                Dictionary<string, double> Students = new Dictionary<string, double>();
                Stream = client.GetStream();
                // получаем имя пользователя
                string message = GetMessage();
                userName = message;

                message = userName + " вошел в систему";
                // посылаем сообщение о входе в чат всем подключенным пользователям
                server.BroadcastMessage(message, this.Id);
                Console.WriteLine(message);
                // в бесконечном цикле получаем сообщения от клиента
                while (true)
                {
                    try
                    {
                        message = GetMessage();
                        if (message != null)
                        {

                            string[] splited = message.Split(" ");
                            switch (splited[0])
                            {
                                case "/exit":
                                    //  Disconnect();
                                    break;
                                case "/PrintStudents":
                                    PrintStudents(Students);
                                    break;
                                case "/AddStudent":
                                    AddStudent(splited, Students);
                                    break;
                                case "/NewMark":
                                    NewMark(splited, Students);
                                    break;
                                case "/DelStudent":
                                    DelStudent(splited, Students);
                                    break;
                                    //default:
                                    //    SendToContact(userName, splited[0], stream);
                                    //    break;


                            }
                            message = String.Format("{0}: {1}", userName, message);
                            Console.WriteLine(message);
                            server.BroadcastMessage(message, this.Id);
                        }
                       
                    }
                    catch
                    {
                        message = String.Format("{0}: покинул чат", userName);
                        Console.WriteLine(message);
                        server.BroadcastMessage(message, this.Id);
                        break;
                    }
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            finally
            {
                // в случае выхода из цикла закрываем ресурсы
                server.RemoveConnection(this.Id);
                Close();
            }
        }
        public void PrintStudents(Dictionary<string, double> Students)
        {
            foreach (var addr in Students)
            {
                for (int i = 0; i < Students.Count; i++)
                Console.WriteLine($"Студент номер {i} " + addr);

            }
        }
        public void AddStudent(string[] message, Dictionary<string, double> Students)
        {
            string value = "";
            string[] splited = message;
            for (int i = 2; i < splited.Length - 2; i++)
            {
                value += splited[i] + " ";
            }
            Students.Add(value, Convert.ToDouble(splited[5]));
        }
        public void NewMark(string[] message, Dictionary<string, double> Students)
        {
            string value = "";
            string[] splited = message;
            for (int i = 2; i < splited.Length -1 ; i++)
            {
                value += splited[i] + " ";
            }
            Students[value] = Convert.ToDouble(message[1]);
        }
        public void DelStudent(string[] message, Dictionary<string, double> Students)
        {
            string value = "";
            string[] splited = message;
            for (int i = 1; i < splited.Length-1; i++)
            {
                value += splited[i] + " ";
            }
            Students.Remove(value);
        }
        
        // чтение входящего сообщения и преобразование в строку
        private string GetMessage()
        {
            NetworkStream ns = Stream;
            byte[] bytes = new byte[client.ReceiveBufferSize];
            do
            {
                ns.Read(bytes, 0, client.ReceiveBufferSize);
            }
            while (ns.DataAvailable);

            string jsonStr = Encoding.UTF8.GetString(bytes);
            Package deserializedWeatherForecast = JsonConvert.DeserializeObject<Package>(jsonStr);
            userName = deserializedWeatherForecast.From;
            return deserializedWeatherForecast.Data;

        }

        // закрытие подключения
        protected internal void Close()
        {
            if (Stream != null)
                Stream.Close();
            if (client != null)
                client.Close();
        }
    }
}
