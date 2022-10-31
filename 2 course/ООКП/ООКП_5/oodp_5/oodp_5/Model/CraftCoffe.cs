using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace oodp_5.Model
{
    public abstract class CraftCoffe
    {
        private readonly CraftCoffe _craftCoffe;
        protected CraftCoffe(CraftCoffe craftCoffe = null)
        {
            _craftCoffe = craftCoffe;
        }
        public virtual string GetCoffeType(string name)
        {
            if(_craftCoffe != null)
            {
                name = _craftCoffe.GetCoffeType(name);
            }
            return name;
        }
    }
}
