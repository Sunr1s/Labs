using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Thelara.Core;
using Thelara.MVVM.ViewModel;
using Thelara.MVVM.Model;
using System.Collections.ObjectModel;
using System.Windows;

namespace Thelara.MVVM.ViewModel
{
   
    class ChiperViewModel : ObservableObject
    {
        public string _address { get; set; }
        public ObservableCollection<MessageModel> Messages { get; set; }
        public ObservableCollection<ContactModel> Contacts { get; set; }

        /* Commands */
        public RelayCommand SendCommand { get; set; }

        private ContactModel _selectedContact;

        public ContactModel SelectedContact
        {
            get { return _selectedContact; }
            set
            {
                _selectedContact = value;
                OnPropertyChanged();
            }
        }


        private string _message;
        public string Message
        {
            get { return _message; }
            set
            {
                _message = value;
                OnPropertyChanged();
            }
        }
        public ChiperViewModel()
        {
            Messages = new ObservableCollection<MessageModel>();
            Contacts = new ObservableCollection<ContactModel>();

            SendCommand = new RelayCommand(o =>
            {
                Messages.Add(new MessageModel
                {
                    Message = Message,
                    FirstMessage = false
                });

                Message = "";

            });


            Messages.Add(new MessageModel
            {
                UserName = "Allison",
                UserNameColor = "#409aff",
                ImageSource = "https://i.imgur.com/yMWvLXd.png",
                Message = "Test",
                Time = DateTime.Now,
                IsNAtiveOrigin = false,
                FirstMessage = true
            });

            for (int i = 0; i < 3; i++)
            {
                Messages.Add(new MessageModel
                {
                    UserName = "Allison",
                    UserNameColor = "#409aff",
                    ImageSource = "https://i.imgur.com/yMWvLXd.png",
                    Message = "Test",
                    Time = DateTime.Now,
                    IsNAtiveOrigin = false,
                    FirstMessage = false
                });
            }

            for (int i = 0; i < 40; i++)
            {
                Messages.Add(new MessageModel
                {
                    UserName = "Bunny",
                    UserNameColor = "#ff3a51",
                    ImageSource = "https://i.imgur.com/yMWvLXd.png",
                    Message = "Test",
                    Time = DateTime.Now,
                    IsNAtiveOrigin = true,
                });
            }

            Messages.Add(new MessageModel
            {
                UserName = "Bunny",
                UserNameColor = "#409aff",
                ImageSource = "https://i.imgur.com/yMWvLXd.png",
                Message = "Last",
                Time = DateTime.Now,
                IsNAtiveOrigin = true,
            });

            for (int i = 0; i < 5; i++)
            {
                Contacts.Add(new ContactModel
                {
                    UserName = $"Allison {i}",
                    ImageSource = "https://i.imgur.com/i2szTsp.png",
                    Messages = Messages
                });
            }
            _selectedContact = Contacts.Last();
        }
        public void ReciverInfo(Network.Node node, string address)
        {
            _address = address;
        }

    }
}
