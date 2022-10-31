using FactoryMethod.Outputer;
using FactoryMethod.Square;

namespace FactoryMethod.Factory
{
    class InscribedFactory : IFactory
    {
        public ISquareByCircle RelaseTriangle() => new Inscribedtriangle();
        public IFormula createResult() => new InscribedTriangle();

    }
}
