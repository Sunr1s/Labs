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

namespace Cinema_BDproject.Domain.Repositories.MongoFramework
{
    public class TextFieldRepos : ITextFieldsRepos
    {
        public IMongoCollection<TextField> TextFields { get; set; }

        public TextFieldRepos(IOptions<MongoDbConfig> mongoDbConfig)
        {
            var mongoClient = new MongoClient(
            mongoDbConfig.Value.ConnectionString);

            var mongoDatabase = mongoClient.GetDatabase(
                mongoDbConfig.Value.Name);

            TextFields = mongoDatabase.GetCollection<TextField>(
                "TextFields");

        }
        public IMongoCollection<TextField> GetTextFields()
        {
           return TextFields;
        }

        public void DeleteTextField(ObjectId id)
        {
            TextFields.DeleteOne(x=>x.Id == id);
        }

        public TextField GetTextFieldByCodeWord(string codeWord)
        {
            return TextFields.Find<TextField>(book => book.CodeWord == codeWord).FirstOrDefault();
            //return TextFields.Find(x => x.CodeWord == codeWord).FirstOrDefault();
        }

        public TextField GetTextFieldById(ObjectId id)
        {
            return TextFields.Find(x => x.Id == id).FirstOrDefault();
        }

        public void SaveTextField(TextField entity)
        {
            var empObj = TextFields.Find(x => x.Id == entity.Id).FirstOrDefault();
            if (empObj != null)
                TextFields.InsertOne(entity);
            else
                TextFields.ReplaceOne(x => x.Id == entity.Id, entity);

        }
    }
}
