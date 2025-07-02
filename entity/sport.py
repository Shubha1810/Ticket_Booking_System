from entity.event import Event


class Sports(Event):
    def __init__(self, event_name='', event_date='', event_time='', venue=None, total_seats=0,
                 ticket_price=0.0, sport_name='', teams_name=''):
        super().__init__(event_name, event_date, event_time, venue, total_seats, ticket_price, 'Sports')
        self.sport_name = sport_name
        self.teams_name = teams_name

    def display_event_details(self):
        super().display_event_details()
        print(f"Sport: {self.sport_name}, Teams: {self.teams_name}")