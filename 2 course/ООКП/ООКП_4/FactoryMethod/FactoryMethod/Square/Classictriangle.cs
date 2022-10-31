using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FactoryMethod.Square
{
    public class Classictriangle : ISquareByCircle
    {
        public double RelaseTriangle(double a, double h, [System.Runtime.InteropServices.Optional] double b, [System.Runtime.InteropServices.Optional] double c)
        {
            return 0.5 * a * h;
        }
    }
}
