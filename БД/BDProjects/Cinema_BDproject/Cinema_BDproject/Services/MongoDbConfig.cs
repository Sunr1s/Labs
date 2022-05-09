using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Cinema_BDproject.Services
{
    public class MongoDbConfig : IMongoDbConfig
    {
        public string Name { get; set; }
        public string Host { get; set; }
        public int Port { get; set; }
        public string ConnectionString => $"mongodb://{Host}:{Port}";

    }

    public interface IMongoDbConfig
    {
        string Name { get; set; }
        string Host { get; set; }
        int Port { get; set; }

        string ConnectionString => $"mongodb://{Host}:{Port}";

    }
}