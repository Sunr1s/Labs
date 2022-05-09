using Cinema_BDproject.Domain.Entities;
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;
using System.ComponentModel.DataAnnotations;

namespace Cinema_BDproject.Domain.Entities
{
    public class ServiceItem : EntityBase
    {
        [Required(ErrorMessage = "Заполните название услуги")]
        [BsonElement("Название услуги")]
        public override string Title { get; set; }

        [BsonElement("Краткое описание услуги")]
        public override string Subtitle { get; set; }

        [BsonElement("Полное описание услуги")]
        public override string Text { get; set; }

        [BsonElement("Актеры")]
        public string[] ActorsName { get; set; }

        [BsonElement("Картинки актеров")]
        public string[] Actorspictures { get; set; }
    }
}
