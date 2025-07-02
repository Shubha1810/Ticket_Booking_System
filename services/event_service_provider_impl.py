from services.i_event_service_provider import IEventServiceProvider
from entity.venue import Venue
from entity.movie import Movie
from entity.concert import Concert
from entity.sport import Sports


class EventServiceProviderImpl(IEventServiceProvider):
    def __init__(self):
        self.events = []

    def create_event(self, event_name, date, time, total_seats, ticket_price, event_type, venue):
        if event_type.lower() == 'movie':
            genre = input("Enter Genre: ")
            actor = input("Enter Actor Name: ")
            actress = input("Enter Actress Name: ")
            event = Movie(event_name, date, time, venue, total_seats, ticket_price, genre, actor, actress)
        elif event_type.lower() == 'concert':
            artist = input("Enter Artist Name: ")
            ctype = input("Enter Concert Type: ")
            event = Concert(event_name, date, time, venue, total_seats, ticket_price, artist, ctype)
        elif event_type.lower() == 'sports':
            sport = input("Enter Sport Name: ")
            teams = input("Enter Teams: ")
            event = Sports(event_name, date, time, venue, total_seats, ticket_price, sport, teams)
        else:
            raise Exception("Invalid event type")
        self.events.append(event)
        return event

    def getEventDetails(self):
        return self.events

    def getAvailableNoOfTickets(self):
        return sum([e.available_seats for e in self.events])
