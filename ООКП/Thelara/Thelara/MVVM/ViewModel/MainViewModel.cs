using Thelara.Core;
using Thelara.MVVM.Model;
using System;
using System.Collections.ObjectModel;
using System.Threading.Tasks;
using System.Windows;
using System.Collections.Generic;


namespace Thelara.MVVM.ViewModel
{
 
    class MainViewModel : ObservableObject
    {
        public ObservableCollection<MessageModel> Messages { get; set; }
        public ObservableCollection<ContactModel> Contacts { get; set; }
       
        public ChiperViewModel chiperView { get; private set; }

        /* Commands */
        
        public RelayCommand SendCommand { get; set; }
        public RelayCommand initChiperWindow { get; set; }
        public RelayCommand AddContact { get; set; }
        public string addr { get; set; }

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

        public MainViewModel()
        {
            Messages = new ObservableCollection<MessageModel>();

            Contacts = new ObservableCollection<ContactModel>();
          //  Network.Node node = CreateNode();
            addr = "127.0.0.1:8089";
            Network.Node node = Network.NewNode(addr);
            Network.Run(node);
           // 

            SendCommand = new RelayCommand(o =>
            {
                Messages.Add(new MessageModel
                {
                    UserName = node.address.IPv4 + ":" + node.address.Port,
                    UserNameColor = "#409aff",
                    ImageSource = "https://i.imgur.com/yMWvLXd.png",
                    Message = Message,
                    Time = DateTime.Now,
                    IsNAtiveOrigin = false,
                    FirstMessage = true,
                });

                node.SendToContact(node, SelectedContact.UserName, Message);

            });
            AddContact = new RelayCommand(o =>
            {
                Contacts.Add(new ContactModel
                {
                    UserName = addr,
                    ImageSource = "https://i.imgur.com/i2szTsp.png",
                    Messages = Messages
                });
                node.Connections.Add(addr, true);
            });

            initChiperWindow = new RelayCommand(o =>
            {
                ChiperViewModel chiperView = new ChiperViewModel();
                chiperView.ReciverInfo(node, addr);
                ChiperWindow chiperWindow = new ChiperWindow();
                chiperWindow.Show();
            });
            foreach (var addres in node.Connections)
            {
                Contacts.Add(new ContactModel
                {
                    UserName = addres.Key,
                    ImageSource = "https://i.imgur.com/i2szTsp.png",
                    Messages = Messages
                }); 
            }

            Task.Factory.StartNew(async () =>
            {
                while (true) 
                {
                    if (Network.recivedMessage != null) 
                    {
                        Application.Current.Dispatcher.Invoke(() =>
                        {
                            Messages.Add(new MessageModel
                            {
                                UserName = Network.actualPackage.From,
                                UserNameColor = "#ff3a51",
                                ImageSource = "https://i.imgur.com/yMWvLXd.png",
                                Message = Network.recivedMessage,
                                Time = DateTime.Now,
                                IsNAtiveOrigin = true,
                                FirstMessage = true
                            });
                        });
                        Network.recivedMessage = null;
                    }
                }
            }); 

        }
 
    }
}
