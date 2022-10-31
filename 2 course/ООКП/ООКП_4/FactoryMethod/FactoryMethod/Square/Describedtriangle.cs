using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FactoryMethod.Square
{
    class Describedtriangle : ISquareByCircle
    {
        public double RelaseTriangle(double a, double b, double c, double R)
        {
            return (a * b * c) / (4 * R);
        }
    }
}
