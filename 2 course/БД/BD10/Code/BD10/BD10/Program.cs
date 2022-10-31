using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using MongoDB.Bson;
using MongoDB.Bson.Serialization;
using MongoDB.Driver;
using MongoDB.Bson.Serialization.Attributes;
using MongoDB.Bson.Serialization.Conventions;

namespace BD10
{
    class Film
    {
        [BsonRepresentation(BsonType.ObjectId)]
        public string Id { get; set; }
        [BsonElement("Film Name")]
        public string FilmName { get; set; }
        [BsonIgnore]
        public string FilmData { get; set; }
        [BsonRepresentation(BsonType.String)]
        public int Duration { get; set; }
        [BsonIgnoreIfNull]
        public Company Actor { get; set; }
    }
    class Film2
    {
        [BsonRepresentation(BsonType.ObjectId)]
        public string Id { get; set; }
        [BsonElement("Film Name")]
        public string FilmName { get; set; }
        [BsonIgnore]
        public string FilmData { get; set; }
        [BsonRepresentation(BsonType.String)]
        public int Duration { get; set; }
        [BsonIgnoreIfNull]
        public Company Actor { get; set; }
    }
    class Company
    {
        public string Name { get; set; }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Film p = new Film {Id = "58506ADE63DD79B8CEAC262E", FilmName = "Santa Barbara", FilmData = "Gates", Duration = 148 };
            p.Actor = new Company { Name = "Bill HArington" };
            Console.WriteLine(p.ToJson());
            Console.ReadKey();

            BsonClassMap.RegisterClassMap<Film2>(cm =>
            {
                cm.AutoMap();
                cm.MapMember(f => f.Id).SetElementName("CC1FF2CC85DC56F4C261E2FD");
                cm.MapMember(f => f.FilmName).SetElementName("Live In Cave");
            });
            Film Film = new Film { FilmName = "Alive", Duration = 144 };
            BsonDocument doc = Film.ToBsonDocument();
            Console.WriteLine(doc);
            Console.ReadLine();

            var conventionPack = new ConventionPack();
            conventionPack.Add(new CamelCaseElementNameConvention());
            ConventionRegistry.Register("idcase", conventionPack, t => true);
            Film = new Film { Id = "58506ADE63DD79B8CEAC263E", FilmName = "Instruction", Duration = 239 };
            doc = Film.ToBsonDocument();
            Console.WriteLine(doc);
            Console.ReadLine();

        }
    }

}
