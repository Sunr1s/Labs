using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace oodp_5.Model
{
    public class AmericanoCraft : CraftCoffe
    {
        public AmericanoCraft(CraftCoffe craftCoffe = null) : base(craftCoffe)
        {

        }
        public override string GetCoffeType(string name)
        {
            var newName = "Американо 50";
            return base.GetCoffeType(newName);
        }
    }
}
