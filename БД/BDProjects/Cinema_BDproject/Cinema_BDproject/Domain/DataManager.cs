using Cinema_BDproject.Domain.Repositories.Abstract;

namespace Cinema_BDproject.Domain
{
    public class DataManager
    {
        public ITextFieldsRepos TextFields { get; set; }
        public IServiceItemRepos ServiceItems { get; set; }

        public DataManager(ITextFieldsRepos textFieldsRepository, IServiceItemRepos serviceItemsRepository)
        {
            TextFields = textFieldsRepository;
            ServiceItems = serviceItemsRepository;
        }
    }
}
