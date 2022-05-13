using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace oodp_5.Model
{
    public  class AddSugar : CraftCoffe
    {
        public AddSugar(CraftCoffe craftCoffe = null) : base(craftCoffe)
        {

        }
       
        public override string GetCoffeType(string nameOfCoffe)
        {
            var WithSugar = "з цукром";
            int Price;
            int.TryParse(string.Join("", nameOfCoffe.Where(c => char.IsDigit(c))), out Price);
            var newPrice= Price + 2;         
            return base.GetCoffeType(nameOfCoffe.Replace(Convert.ToString(Price), Convert.ToString(newPrice)) + " "+ WithSugar);
        }
    }
}
