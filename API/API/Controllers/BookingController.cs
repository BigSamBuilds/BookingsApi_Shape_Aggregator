using BookingsApi.Models;
using BookingsApi.Services;
using Microsoft.AspNetCore.Mvc;
using System.Net;

namespace BookingsApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class BookingsController : ControllerBase
    {
        //private readonly BookingService _service = new BookingService();
        private readonly IBookingService _service;
        public BookingsController(IBookingService service)
        {
            _service = service;
        }

        [HttpGet]
        public IActionResult GetAll()
        {
            return Ok(_service.GetAll());
        }

        [HttpGet("{id:int}")]
        public IActionResult GetById(int id)
        {
            var booking = _service.GetById(id);
            return booking == null ? NotFound() : Ok(booking);
        }

        [HttpPost]
        public IActionResult Create([FromBody] Booking booking)
        {
            try
            {
                var created = _service.Create(booking);

                return CreatedAtAction(nameof(GetById), new { id = created.Id }, created);
            }
            catch (InvalidOperationException ex)
            {
                /*
                 * Error kan loggas i en log fill, eller skrivas ut.
                 * Console.write(ex) OR Log.log(ex) 
                 */

                return Conflict(ex.Message);
            }
            catch (Exception ex)
            {

                /* Detta om man vill logga filet och klienten skall inte se backend error.
                 * Log(ex)
                 */
                return StatusCode(500);
            }

        }

        [HttpDelete("{id:int}")]
        public IActionResult DeleteById(int id)
        {
            try
            {
                var boking = _service.GetById(id);
                if (boking != null)
                {
                    _service.Cancel(id);
                    return NoContent();
                }
                return NotFound();
            } catch (Exception ex)
            {
                /*  om man vill logga fajlet och klienten skall inte se backend error.
                 * Log(ex)
                 */
                return StatusCode(500);
            }
            
        }

    }
}
