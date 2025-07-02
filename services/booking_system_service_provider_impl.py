from services.i_booking_system_service_provider import IBookingSystemServiceProvider
from services.event_service_provider_impl import EventServiceProviderImpl
from entity.booking import Booking


class BookingSystemServiceProviderImpl(EventServiceProviderImpl, IBookingSystemServiceProvider):
    def __init__(self):
        super().__init__()
        self.bookings = []

    def calculate_booking_cost(self, num_tickets, ticket_price):
        return num_tickets * ticket_price

    def book_tickets(self, event_name, num_tickets, customers):
        for e in self.events:
            if e.event_name == event_name:
                if len(customers) != num_tickets:
                    raise Exception("Mismatch in customer count")
                if e.book_tickets(num_tickets):
                    booking = Booking(customers, e, num_tickets)
                    self.bookings.append(booking)
                    return booking
        raise Exception("Event not found or tickets unavailable")

    def cancel_booking(self, booking_id):
        for b in self.bookings:
            if b.booking_id == booking_id:
                b.event.cancel_booking(b.num_tickets)
                self.bookings.remove(b)
                return True
        raise Exception("Invalid Booking ID")

    def get_booking_details(self, booking_id):
        for b in self.bookings:
            if b.booking_id == booking_id:
                return b
        raise Exception("Booking not found")
