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
        public string ConnectionString => $"mongodb://david1337:FOcY9lgX4mHEujcZj985Y8fQWQGq8TW7vk5Hbj2usb4U5dF9KRjCsVjjiebLvrZbiE3FLblvlJnvTG25qsjISQ==@david1337.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@david1337@";

    }

    public interface IMongoDbConfig
    {
        string Name { get; set; }
        string Host { get; set; }
        int Port { get; set; }

        string ConnectionString => $"mongodb://{Host}:{Port}";

    }
}
