using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MongoDB.Bson;
using MongoDB.Driver;
using System.Configuration;

namespace BD9
{
    class Program
    {
       
		static void Main(string[] args)
		{
			string con =
				ConfigurationManager.ConnectionStrings["MongoDb"].ConnectionString;
				MongoClient client = New MongoClient(con);
				GetDatabaseNames(client).GetAwaiter();
			Console.ReadLine();
		}
		private static async Task GetDatabaseNames(MongoClient client)
		{
			using (var cursor = await client.ListDatabasesAsync())
			 {
				 var databaseDocuments = await cursor.ToListAsync();
				foreach (var databaseDocument in databaseDocuments){
				Console.WriteLine(databaseDocument["name"]);
				}
			}
		 }
	 }
}
