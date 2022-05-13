using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace oodp_5.Model
{
    public class LatteCraft : CraftCoffe
    {
        public LatteCraft(CraftCoffe craftCoffe = null) : base(craftCoffe)
        {

        }
        public override string GetCoffeType(string name)
        {
            var newName = "Латте 40";
            return base.GetCoffeType(newName);
        }
    }
}
