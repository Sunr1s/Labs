using FactoryMethod.Outputer;
using FactoryMethod.Square;

namespace FactoryMethod.Factory
{
    class ClassicFactory : IFactory
    {
        public ISquareByCircle RelaseTriangle() => new Classictriangle();
        public IFormula createResult() => new ClassicTriangle();

    }

}
