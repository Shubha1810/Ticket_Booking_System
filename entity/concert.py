from entity.event import Event


class Concert(Event):
    def __init__(self, event_name='', event_date='', event_time='', venue=None, total_seats=0,
                 ticket_price=0.0, artist='', concert_type=''):
        super().__init__(event_name, event_date, event_time, venue, total_seats, ticket_price, 'Concert')
        self.artist = artist
        self.concert_type = concert_type

    def display_event_details(self):
        super().display_event_details()
        print(f"Artist: {self.artist}, Type: {self.concert_type}")