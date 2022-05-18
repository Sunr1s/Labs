using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using MongoDB.Bson;
using MongoDB.Driver;
using MongoDB.Driver.Linq;

namespace BD12
{
    class Program
    {
        static string connectionString = "mongodb://localhost";
        static MongoClient client = new MongoClient(connectionString);
        static IMongoDatabase database = client.GetDatabase("test");
        static IMongoCollection<BsonDocument> collection = database.GetCollection<BsonDocument>("Films");
        static BsonDocument filter = new BsonDocument();
        static void Main(string[] args)
        {
            FindDocs().GetAwaiter().GetResult();
            Console.ReadLine();
            FindDocs2().GetAwaiter().GetResult();
            Console.ReadLine();
        }
        private static async Task FindDocs()
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
        private static async Task FindDocs2()
        {
          
            var people = await collection.Find(filter).ToListAsync();
            foreach (var doc in people)
            {
                Console.WriteLine(doc);
            }
        }
    }
}
