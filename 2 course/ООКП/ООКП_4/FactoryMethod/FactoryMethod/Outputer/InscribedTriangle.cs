using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FactoryMethod.Outputer
{
    class InscribedTriangle : IFormula
    {
        public void PrintResult(ISquareByCircle squareByCircle)
        {
            Console.WriteLine("Результат за формулой вписаного кола: " + squareByCircle.RelaseTriangle(3, 4, 2, 0.6667).ToString());

        }
    }
}
