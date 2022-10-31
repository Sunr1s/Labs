using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Cinema_BDproject.Domain.Entities;
using Cinema_BDproject.Domain.Repositories.Abstract;
using Cinema_BDproject.Services;
using Microsoft.Extensions.Options;
using MongoDB.Bson;
using MongoDB.Driver;
using MongoDB.Driver.Linq;

namespace Cinema_BDproject.Domain.Repositories.MongoFramework
{
    public class ServiceRepos : IServiceItemRepos
    {
        public IMongoCollection<ServiceItem> ServiceItems { get; set; }

        public ServiceRepos(IOptions<MongoDbConfig> mongoDbConfig)
        {
            var mongoClient = new MongoClient(
            mongoDbConfig.Value.ConnectionString);

            var mongoDatabase = mongoClient.GetDatabase(
                mongoDbConfig.Value.Name);

            ServiceItems = mongoDatabase.GetCollection<ServiceItem>(
                "ServiceItems");

        }
        public void DeleteServiceItem(ObjectId id)
        {
            ServiceItems.DeleteOne(x => x.Id == id);
        }

        public ServiceItem GetServiceItemById(ObjectId id)
        {
            return ServiceItems.Find(x => x.Id == id).FirstOrDefault();
        }

        public IMongoQueryable<ServiceItem> GetServiceItems()
        {
            return ServiceItems.AsQueryable<ServiceItem>();
        }

        public void SaveServiceItem(ServiceItem entity)
        {
            var empObj = ServiceItems.Find(x => x.Id == entity.Id).FirstOrDefault();
            if (empObj != null)
                ServiceItems.InsertOne(entity);
            else
                ServiceItems.ReplaceOne(x => x.Id == entity.Id, entity);
        }
    }
}
