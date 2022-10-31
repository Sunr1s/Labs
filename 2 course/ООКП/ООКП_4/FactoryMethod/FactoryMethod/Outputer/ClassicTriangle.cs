using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FactoryMethod.Outputer
{
    class ClassicTriangle : IFormula
    {
        public void PrintResult(ISquareByCircle squareByCircle)
        {
            Console.WriteLine("Результат за класичною формулою: " + squareByCircle.RelaseTriangle(3, 2 ,0,0).ToString());
        }
    }
}
