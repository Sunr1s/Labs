using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using MongoDB.Bson;
using MongoDB.Driver;


namespace BD11
{
    class Person
    {
        public ObjectId Id { get; set; }
        public string Name { get; set; }
        public int Time { get; set; }
        public Company Studia { get; set; }
        public List<string> Languages { get; set; }
    }
    class Company
    {
        public string Name { get; set; }
    }
    class Program
    {
        static BsonDocument filter = new BsonDocument();
        static void Main(string[] args)
        {
            string connectionString = "mongodb://localhost";
            var client = new MongoClient(connectionString);
            var database = client.GetDatabase("test");
            var collection = database.GetCollection<BsonDocument>("Films");
           
            SaveDocs(collection).GetAwaiter().GetResult();
            SaveFewDocs(collection).GetAwaiter().GetResult();
            var collection2 = database.GetCollection<Person>("Films");
            SaveDocsByClass(connectionString, client, collection2, database).GetAwaiter().GetResult();

            FindDocs(collection).GetAwaiter().GetResult();
            Console.ReadLine();
            FindDocs2(collection).GetAwaiter().GetResult();
            Console.ReadLine();

            Console.ReadLine();
        }
        private static async Task FindDocs(IMongoCollection<BsonDocument> collection)
        {

            using (var cursor = await collection.FindAsync(filter))
            {
                while (await cursor.MoveNextAsync())
                {
                    var people = cursor.Current;
                    foreach (var doc in people)
                    {
                
                        Console.WriteLine(doc);
                    }
                }

            }
        }
        private static async Task FindDocs2(IMongoCollection<BsonDocument> collection)
        {

            var people = await collection.Find(filter).ToListAsync();
            foreach (var doc in people)
            {
                Console.WriteLine(doc);
            }
        }
        private static async Task SaveDocs(IMongoCollection<BsonDocument> collection)
        {
            BsonDocument person1 = new BsonDocument
             {
             {"Name", "Happy year"},
             {"Time", 302},
             {"Languages", new BsonArray{"english", "german"}}
             };
            await collection.InsertOneAsync(person1);
        }
        private static async Task SaveFewDocs(IMongoCollection<BsonDocument> collection)
        {
            BsonDocument person1 = new BsonDocument
             {
             {"Name", "The Shawshank Redemption"},
             {"Time", 145},
             {"Languages", new BsonArray{"english", "german"}}
             };
            BsonDocument person2 = new BsonDocument
            {
             {"Name", "The Godfather"},
             {"Time", 234},
             {"Languages", new BsonArray{"english", "german"}}
             };
            await collection.InsertManyAsync(new[] { person1, person2 });
        }
        private static async Task SaveDocsByClass(string connectionString, MongoClient client, IMongoCollection<Person> collection, IMongoDatabase database)
        {
            Person person1 = new Person
            {
                Name = "12 Angry Men",
                Time = 209,
                Languages = new List<string> { "english", "german" },
                Studia = new Company
                {
                    Name = "Holiwood"
                }
            };
            await collection.InsertOneAsync(person1);
            Console.WriteLine(person1.Id);
        }
    }
}

