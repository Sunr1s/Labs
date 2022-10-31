using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;
using System.ComponentModel.DataAnnotations;

namespace Cinema_BDproject.Domain.Entities
{
    [BsonIgnoreExtraElements]
    public class TextField : EntityBase
    {
        [Required]
        [BsonElement("Название страницы (заголовок)")]
        public override string Title { get; set; } = "Информационная страница";
        [Required]
        public string CodeWord { get; set; }
        [Required]

        [BsonElement("Cодержание страницы")]
        public override string Text { get; set; } = "Содержание заполняется администратором";
    }
}
