from abc import ABC, abstractmethod


class BookingSystem(ABC):
    @abstractmethod
    def create_event(self, event_name, event_date, event_time, total_seats, ticket_price, event_type, venue_name,
                     address):
        pass

    @abstractmethod
    def book_tickets(self, event, customer, num_tickets):
        pass

    @abstractmethod
    def cancel_tickets(self, booking_id):
        pass

    @abstractmethod
    def display_event_details(self, event):
        pass
