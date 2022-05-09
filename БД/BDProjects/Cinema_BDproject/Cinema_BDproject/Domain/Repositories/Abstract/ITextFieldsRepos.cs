using Cinema_BDproject.Domain.Entities;
using MongoDB.Bson;
using MongoDB.Driver;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Cinema_BDproject.Domain.Repositories.Abstract
{
    public interface ITextFieldsRepos
    {
        IMongoCollection<TextField> GetTextFields();
        TextField GetTextFieldById(ObjectId id);
        TextField GetTextFieldByCodeWord(string codeWord);
        void SaveTextField(TextField entity);
        void DeleteTextField(ObjectId id);
    }
}
