class Venue:
    def __init__(self, venue_name='', address=''):
        self.venue_name = venue_name
        self.address = address

    def display_venue_details(self):
        print(f"Venue: {self.venue_name}, Address: {self.address}")

