using System;
using FactoryMethod.Factory;

namespace FactoryMethod
{
    class Program
    {
        static void Main(string[] args)
        {
            IFactory innerfactory = new InscribedFactory();
            ISquareByCircle innerCircle = innerfactory.RelaseTriangle();
            IFormula innerFormula = innerfactory.createResult();

            innerFormula.PrintResult(innerCircle);

            IFactory outfactory = new DescribedFactory();
            ISquareByCircle outCircle = outfactory.RelaseTriangle();
            IFormula outFormula = outfactory.createResult();

            outFormula.PrintResult(outCircle);

            IFactory clsfactory = new ClassicFactory();
            ISquareByCircle clsSquare = clsfactory.RelaseTriangle();
            IFormula clsFormula = clsfactory.createResult();

            clsFormula.PrintResult(clsSquare);
        }
    }
}
