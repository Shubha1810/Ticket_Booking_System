from entity.customer import Customer
from entity.booking import Booking
from entity.venue import Venue
from entity.movie import Movie
from entity.concert import Concert
from entity.sport import Sports
from services.booking_system import BookingSystem
from exception.event_not_found_exception import EventNotFoundException
from exception.invalid_booking_id_exception import InvalidBookingIDException
from util.db_util import DBUtil
from datetime import datetime


class TicketBookingSystem(BookingSystem):
    def __init__(self):
        self.events = set()
        self.bookings = set()
        self.venues = set()
        self.customers = set()

        self.load_venues_from_db()
        self.load_events_from_db()
        self.load_customers_from_db()
        self.load_bookings_from_db()

    def create_event(self, event_name, event_date, event_time, total_seats, ticket_price, event_type, venue_city,
                     address):
        try:
            if not event_date.strip():
                print("❌ Event date is required.")
                return None

            # Insert venue into DB if not already existing (optional: handle duplicates properly)
            conn = DBUtil.get_db_conn()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO venue (venue_name, address) VALUES (%s, %s)", (venue_city, address))
            venue_id = cursor.lastrowid
            conn.commit()

            # Insert event into event table
            cursor.execute(
                "INSERT INTO event (event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (event_name, event_date, event_time, venue_id, total_seats, total_seats, ticket_price,
                 event_type.lower())
            )
            event_id = cursor.lastrowid
            conn.commit()

            # Create in-memory Venue and Event object
            venue = Venue(venue_city, address)

            if event_type.lower() == 'movie':
                genre = input("Enter Genre: ")
                actor = input("Enter Actor Name: ")
                actress = input("Enter Actress Name: ")
                event = Movie(event_name, event_date, event_time, venue, total_seats, ticket_price, genre, actor,
                              actress)

                # Insert into movie table
                cursor.execute("INSERT INTO movie (event_id, genre, actor_name, actress_name) VALUES (%s, %s, %s, %s)",
                               (event_id, genre, actor, actress))

            elif event_type.lower() == 'concert':
                artist = input("Enter Artist Name: ")
                ctype = input("Enter Concert Type (Theatrical/Classical/Rock/Recital): ")
                event = Concert(event_name, event_date, event_time, venue, total_seats, ticket_price, artist, ctype)

                # Insert into concert table
                cursor.execute("INSERT INTO concert (event_id, artist_name, concert_type) VALUES (%s, %s, %s)",
                               (event_id, artist, ctype))

            elif event_type.lower() == 'sports':
                sport = input("Enter Sport Name: ")
                teams = input("Enter Teams (e.g., India vs Pakistan): ")
                event = Sports(event_name, event_date, event_time, venue, total_seats, ticket_price, sport, teams)

                # Insert into sports table
                cursor.execute("INSERT INTO sports (event_id, sport_name, teams_name) VALUES (%s, %s, %s)",
                               (event_id, sport, teams))

            else:
                raise ValueError("Invalid event type")

            conn.commit()
            conn.close()

            self.events.add(event)
            print(" Event created and saved to database successfully.")
            print(f" Event ID: {event_id}, Name: {event_name}")
            return event_id

        except Exception as e:
            print(f"Error creating event: {e}")
            return None

    def book_tickets(self, event_name, num_tickets, customers):
        for event in self.events:
            if event.event_name == event_name:
                if len(customers) != num_tickets:
                    raise ValueError("Number of customers must match number of tickets")

                if event.book_tickets(num_tickets):
                    booking = Booking(customers, event, num_tickets)
                    self.bookings.add(booking)
                    return booking
                else:
                    raise Exception("Tickets unavailable")
        raise EventNotFoundException()

    def cancel_tickets(self, booking_id):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                booking.event.cancel_booking(booking.num_tickets)
                self.bookings.remove(booking)
                return True
        raise InvalidBookingIDException()

    def display_event_details(self, event):
        try:
            print(f"Event: {event.event_name}, Type: {event.event_type}, Venue City: {event.venue.venue_name}")
            event.display_event_details()
        except Exception as e:
            print(f"Error displaying event details: {e}")

    def get_sorted_events(self):
        return sorted(self.events, key=lambda e: (e.event_name.lower(), e.venue.venue_name.lower()))

    def load_venues_from_db(self):
        conn = DBUtil.get_db_conn()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM venue")
        for row in cursor.fetchall():
            venue = Venue(row['venue_name'], row['address'])
            self.venues.add(venue)
        conn.close()

    def load_events_from_db(self):
        conn = DBUtil.get_db_conn()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT e.*, v.venue_name, v.address
            FROM event e
            JOIN venue v ON e.venue_id = v.venue_id
        """)
        for row in cursor.fetchall():
            venue = Venue(row['venue_name'], row['address'])
            if row['event_type'] == 'movie':
                event = Movie(row['event_name'], row['event_date'], row['event_time'], venue,
                              row['total_seats'], row['ticket_price'], "", "", "")
            elif row['event_type'] == 'concert':
                event = Concert(row['event_name'], row['event_date'], row['event_time'], venue,
                                row['total_seats'], row['ticket_price'], "", "")
            elif row['event_type'] == 'sports':
                event = Sports(row['event_name'], row['event_date'], row['event_time'], venue,
                               row['total_seats'], row['ticket_price'], "", "")
            else:
                continue  # skip unknown types
            self.events.add(event)
        conn.close()

    def load_customers_from_db(self):
        conn = DBUtil.get_db_conn()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM customer")
        for row in cursor.fetchall():
            customer = Customer(row['customer_name'], row['email'], row['phone_number'])
            self.customers.add(customer)
        conn.close()

    def load_bookings_from_db(self):
        conn = DBUtil.get_db_conn()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT b.booking_id, b.num_tickets, b.total_cost, b.booking_date,
                   c.customer_name, c.email, c.phone_number,
                   e.event_name, e.event_date, e.event_time, e.ticket_price, e.event_type,
                   v.venue_name, v.address
            FROM booking b
            JOIN customer c ON b.customer_id = c.customer_id
            JOIN event e ON b.event_id = e.event_id
            JOIN venue v ON e.venue_id = v.venue_id
        """)
        for row in cursor.fetchall():
            customer = Customer(row['customer_name'], row['email'], row['phone_number'])
            venue = Venue(row['venue_name'], row['address'])

            event_type = row.get('event_type', '').lower()
            if event_type == 'movie':
                event = Movie(row['event_name'], row['event_date'], row['event_time'], venue,
                              0, row['ticket_price'], '', '', '')
            elif event_type == 'concert':
                event = Concert(row['event_name'], row['event_date'], row['event_time'], venue,
                                0, row['ticket_price'], '', '')
            elif event_type == 'sports':
                event = Sports(row['event_name'], row['event_date'], row['event_time'], venue,
                               0, row['ticket_price'], '', '')
            else:
                continue  # skip if unknown

            booking = Booking([customer], event, row['num_tickets'], row['total_cost'], row['booking_date'])
            booking.booking_id = row['booking_id']
            self.bookings.add(booking)
        conn.close()
