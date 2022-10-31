using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using oodp_5.Model;
using oodp_5.Core;
using System.Windows;

namespace oodp_5.Presenter
{
    public class CoffePresenter
    {
        public RelayCommand BuyEspresso { get; set; }
        public RelayCommand BuyLatte { get; set; }
        public RelayCommand BuyCappuccino { get; set; }
        public RelayCommand BuyAmericano { get; set; }
        public RelayCommand addSugar { get; set; }
        AddSugar addsugar = null;
        public RelayCommand addMilk { get; set; }
        AddMilk addmilk = null;
        public CoffePresenter()
        {
            var text = "coffe";
          
            addSugar = new RelayCommand(o =>
            {
                addsugar = new AddSugar();
            });
            addMilk = new RelayCommand(o =>
            {
                addmilk = new AddMilk();
            });

            BuyEspresso = new RelayCommand(o =>
            {
                var newcoffe = new EspressoCraft(addsugar);
                
                MessageBox.Show(newcoffe.GetCoffeType(text));
                addsugar = null;
            });
            BuyLatte = new RelayCommand(o =>
            {
                var newcoffe = new LatteCraft(addsugar);

                MessageBox.Show(newcoffe.GetCoffeType(text));
                addsugar = null;
            });
            BuyCappuccino = new RelayCommand(o =>
            {
                var newcoffe = new CappuccinoCraft(addsugar);

                MessageBox.Show(newcoffe.GetCoffeType(text));
                addsugar = null;
            });
            BuyAmericano = new RelayCommand(o =>
            {
                var newcoffe = new AmericanoCraft(addsugar);

                MessageBox.Show(newcoffe.GetCoffeType(text));
                addsugar = null;
            });

        }

    }
}
