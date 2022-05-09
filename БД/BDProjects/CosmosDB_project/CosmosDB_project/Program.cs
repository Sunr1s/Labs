using Microsoft.Azure.Cosmos;
using System;
using System.Threading.Tasks;

namespace CosmosDB_project
{
    internal class Program
    {
        static void Main(string[] args)
        {
            CreateItem().Wait();
        }
        private static async Task CreateItem()
        {
            var cosmosUrl = "https://david1337.documents.azure.com:443/";
            var cosmoskey = "FOcY9lgX4mHEujcZj985Y8fQWQGq8TW7vk5Hbj2usb4U5dF9KRjCsVjjiebLvrZbiE3FLblvlJnvTG25qsjISQ==";
            var databaseName = "FilmsDB";

            CosmosClient client = new CosmosClient(cosmosUrl, cosmoskey);
            Database database = await client.CreateDatabaseIfNotExistsAsync(databaseName);
            Container container = await database.CreateContainerIfNotExistsAsync(
                "MyContainerName", "/partitionKeyPath", 1000);

            dynamic testItem = new { id = Guid.NewGuid().ToString(), partitionKeyPath = "MyTestPkValue", details = "it's working" };
            ItemResponse<dynamic> response = await container.CreateItemAsync(testItem);
        }
    }
}
