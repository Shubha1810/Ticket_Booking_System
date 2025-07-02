from abc import ABC, abstractmethod


class Event(ABC):
    def __init__(self, event_name='', event_date='', event_time='', venue=None, total_seats=0, ticket_price=0.0,
                 event_type=''):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue = venue
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.ticket_price = ticket_price
        self.event_type = event_type

    def calculate_total_revenue(self):
        return (self.total_seats - self.available_seats) * self.ticket_price

    def get_booked_no_of_tickets(self):
        return self.total_seats - self.available_seats

    def book_tickets(self, num_tickets):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            return True
        else:
            return False

    def cancel_booking(self, num_tickets):
        self.available_seats += num_tickets

    @abstractmethod
    def display_event_details(self):
        pass
