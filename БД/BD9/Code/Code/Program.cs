using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MongoDB.Bson;
using MongoDB.Driver;
using System.Configuration;
using Microsoft.Extensions.Configuration;
using MongoDB.Bson.Serialization;
using System.Security.Authentication;

namespace BD9
{
    class FilmStudio
    {
        public ObjectId Id { get; set; }
        public string country { get; set; }
        public string name { get; set; }
        public string legal_address { get; set; }
        public Actors actors { get; set; }
    }
    class Actors
    {
        public string Name { get; set; }
        public string gender { get; set; }

    }
    class Program
    {

        static void Main(string[] args)
        {
            string connectionString =
   @"mongodb://david1337:FOcY9lgX4mHEujcZj985Y8fQWQGq8TW7vk5Hbj2usb4U5dF9KRjCsVjjiebLvrZbiE3FLblvlJnvTG25qsjISQ==@david1337.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@david1337@";
            MongoClientSettings settings = MongoClientSettings.FromUrl(
              new MongoUrl(connectionString)
            );

            settings.SslSettings =
              new SslSettings() { EnabledSslProtocols = SslProtocols.Tls12 };
            var client = new MongoClient(settings);
            Console.WriteLine("");
            Console.WriteLine("Отримання всiх бд iз сервера");
            Console.WriteLine("");
            GetDatabaseNames(client).GetAwaiter();
            Console.ReadLine();

            Console.WriteLine("");
            Console.WriteLine("Отримаємо всi колекцiї всiх баз даних, якi є на серверi");
            Console.WriteLine("");
            GetCollectionsNames(client).GetAwaiter();
            Console.ReadLine();

            Console.WriteLine("");
            Console.WriteLine("Створимо модель даних");
            Console.WriteLine("");
            SimpleDocument();



            Console.WriteLine("");
            Console.WriteLine(". При створеннi документа ми можемо скористатися як стандартним класом C#, так i класом BsonDocument");
            Console.WriteLine("");
            BSONDocument();



            Console.ReadLine();

        }
        private static async Task GetDatabaseNames(MongoClient client)
        {
            using (var cursor = await client.ListDatabasesAsync())
            {
                var databaseDocuments = await cursor.ToListAsync();
                foreach (var databaseDocument in databaseDocuments)
                {
                    Console.WriteLine(databaseDocument["name"]);
                }
            }
        }
        private static async Task GetCollectionsNames(MongoClient client)
        {
            using (var cursor = await client.ListDatabasesAsync())

            {
                var dbs = await cursor.ToListAsync();
                foreach (var db in dbs)
                {
                    Console.WriteLine("У базi даних {0} є наступнi колекцii:", db["name"]);
                    IMongoDatabase database = client.GetDatabase(db["name"].ToString());
                    using (var collCursor = await database.ListCollectionsAsync())
                    {
                        var colls = await collCursor.ToListAsync();
                        foreach (var col in colls)
                        {
                            Console.WriteLine(col["name"]);
                        }
                    }
                    Console.WriteLine();
                }
            }
        }
        private static async Task SimpleDocument()
        {
            FilmStudio filmStudio = new FilmStudio { country = "Ukraine", name = "GasMyas", legal_address = "st Avenue, 1" };
            filmStudio.actors = new Actors { Name = "Ryan Mertviy", gender = "male" };
            Console.WriteLine(filmStudio.ToJson());
            Console.WriteLine("");
            Console.WriteLine("Також можна виконати зворотну операцiю перетворення об'єкта в BsonDocument");
            Console.WriteLine("");
            ObjectToBson(filmStudio);
        }
        private static async Task BSONDocument()
        {
            BsonDocument doc = new BsonDocument
            {
                {"country","Ukraine"},
                {"name", "GasMyas"},
                {"legal_address", "st Avenue, 1"},
                { "actors",
                    new BsonDocument
                    {
                         {"Name" , "Ryan Mertviy" },
                         { "gender" , "male"}
                    }
                }
            };
            FilmStudio p = BsonSerializer.Deserialize<FilmStudio>(doc);
            Console.WriteLine(p.ToJson());
        }
        private static async Task ObjectToBson(FilmStudio filmStudio)
        {
            BsonDocument doc = filmStudio.ToBsonDocument();
            Console.WriteLine(doc);
        }
    }
}
