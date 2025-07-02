from abc import ABC, abstractmethod


class IEventServiceProvider(ABC):
    @abstractmethod
    def create_event(self, event_name, date, time, total_seats, ticket_price, event_type, venue): pass

    @abstractmethod
    def getEventDetails(self): pass

    @abstractmethod
    def getAvailableNoOfTickets(self): pass
