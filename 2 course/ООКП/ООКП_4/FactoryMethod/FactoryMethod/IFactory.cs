using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FactoryMethod
{
    interface IFactory
    {
        ISquareByCircle RelaseTriangle();
        IFormula createResult();
    }
}
