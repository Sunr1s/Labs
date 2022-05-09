using Cinema_BDproject.Domain.Entities;
using MongoDB.Bson;
using MongoDB.Driver;
using MongoDB.Driver.Linq;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Cinema_BDproject.Domain.Repositories.Abstract
{
    public interface IServiceItemRepos
    {
        IMongoQueryable<ServiceItem> GetServiceItems();
        ServiceItem GetServiceItemById(ObjectId id);
        void SaveServiceItem(ServiceItem entity);
        void DeleteServiceItem(ObjectId id);

    }
}
