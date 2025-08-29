using BookingsApi.Models;

namespace BookingsApi.Repositories
{
    public interface IBookingRepository
    {

        public IEnumerable<Booking> GetAll();

        public Booking? GetById(int id);

        public Booking Add(Booking booking);

        public void Delete(int id);
    }
}
