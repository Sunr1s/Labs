using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FactoryMethod.Square
{
    class Inscribedtriangle : ISquareByCircle
    {
        public double RelaseTriangle(double a, double b, double c, double r)
        {
            return r * (a + b + c) / 2;
        }
    }
}
