from abc import ABC, abstractmethod


class IBookingSystemRepository(ABC):
    @abstractmethod
    def create_event(self, event): pass

    @abstractmethod
    def get_event_details(self): pass

    @abstractmethod
    def get_available_no_of_tickets(self): pass

    @abstractmethod
    def calculate_booking_cost(self, num_tickets, price): pass

    @abstractmethod
    def book_tickets(self, event_name, num_tickets, customers): pass

    @abstractmethod
    def cancel_booking(self, booking_id): pass

    @abstractmethod
    def get_booking_details(self, booking_id): pass
