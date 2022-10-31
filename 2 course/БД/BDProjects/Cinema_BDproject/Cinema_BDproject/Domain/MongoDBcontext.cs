using MongoDB.Driver;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Configuration;
using Cinema_BDproject.Domain.Entities;
namespace Cinema_BDproject.Domain
{
    public class MongoDBcontext
    {

        public MongoClient client { get; set; }
        public IMongoDatabase database { get; set; }

        public IMongoCollection<TextField> TextFields { get; set; }
        public IMongoCollection<ServiceItem> ServiceItems { get; set; }

        //public MongoDBcontext()
        //{
        //    var mongoClient = new MongoClient(ConfigurationManager);

        //}
    }
}
