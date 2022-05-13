using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FactoryMethod.Outputer
{
    class DescribedTriangle : IFormula
    {
        public void PrintResult(ISquareByCircle squareByCircle)
        {
            Console.WriteLine("Результат за формулой описаного кола: " + squareByCircle.RelaseTriangle(3, 2, 4, 2).ToString());

        }
    }
}
