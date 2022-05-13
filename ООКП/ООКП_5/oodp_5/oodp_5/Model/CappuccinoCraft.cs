using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace oodp_5.Model
{
    public class CappuccinoCraft : CraftCoffe
    {
        public CappuccinoCraft(CraftCoffe craftCoffe = null) : base(craftCoffe)
        {

        }
        public override string GetCoffeType(string name)
        {
            var newName = "Каппуччино 45";
            return base.GetCoffeType(newName);
        }
    }
}
