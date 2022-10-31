using FactoryMethod.Outputer;
using FactoryMethod.Square;

namespace FactoryMethod.Factory
{
    class DescribedFactory : IFactory
    {
        public ISquareByCircle RelaseTriangle() => new Describedtriangle();
        public IFormula createResult() => new DescribedTriangle();

    }
}
