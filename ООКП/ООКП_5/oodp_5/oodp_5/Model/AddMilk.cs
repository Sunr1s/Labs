using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace oodp_5.Model
{
    public class AddMilk : CraftCoffe
    {
        public AddMilk(CraftCoffe craftCoffe = null) : base(craftCoffe)
        {

        }
        public override string GetCoffeType(string name)
        {
            var newName = "c молоком";
            return base.GetCoffeType(name + " " + newName);
        }
    }
}
