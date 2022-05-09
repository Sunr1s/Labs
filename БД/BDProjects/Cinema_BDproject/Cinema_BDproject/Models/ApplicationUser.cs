using AspNetCore.Identity.MongoDbCore.Models;
using MongoDbGenericRepository.Attributes;
using System;

namespace Cinema_BDproject.Models
{

    [CollectionName("Users")]
    public class ApplicationUser : MongoIdentityUser<Guid>
    {
    }

}
