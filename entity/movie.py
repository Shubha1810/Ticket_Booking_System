from entity.event import Event


class Movie(Event):
    def __init__(self, event_name='', event_date='', event_time='', venue=None, total_seats=0,
                 ticket_price=0.0, genre='', actor_name='', actress_name=''):
        super().__init__(event_name, event_date, event_time, venue, total_seats, ticket_price, 'Movie')
        self.genre = genre
        self.actor_name = actor_name
        self.actress_name = actress_name

    def display_event_details(self):
        super().display_event_details()
        print(f"Genre: {self.genre}, Actor: {self.actor_name}, Actress: {self.actress_name}")