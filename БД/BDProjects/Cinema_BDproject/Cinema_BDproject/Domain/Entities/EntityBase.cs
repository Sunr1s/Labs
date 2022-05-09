using System;
using System.ComponentModel.DataAnnotations;
using MongoDB.Bson.Serialization;
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;
using MongoDB.Bson.Serialization.IdGenerators;

namespace Cinema_BDproject.Domain.Entities
{
    public abstract class EntityBase
    {
        [BsonId(IdGenerator = typeof(StringObjectIdGenerator))]
        [BsonRequired]
        public ObjectId Id { get;set; }

        [BsonElement("Название (заголовок)")]
        public virtual string Title { get; set; }

        [BsonElement("Краткое описание")]
        public virtual string Subtitle { get; set; }

        [BsonElement("Полное описание")]
        public virtual string Text { get; set; }

        [BsonElement("Титульная картинка")]
        public virtual string TitleImagePath { get; set; }

        [BsonElement("SEO метатег Title")]
        public string MetaTitle { get; set; }

        [BsonElement("SEO метатег Description")]
        public string MetaDescription { get; set; }

        [BsonElement("SEO метатег Keywords")]
        public string MetaKeywords { get; set; }

        [BsonDateTimeOptions(Kind = DateTimeKind.Local)]
        public DateTime DateAdded { get; set; }
    }
}
