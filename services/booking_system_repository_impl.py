from services.booking_system_repository import IBookingSystemRepository
from util.db_util import DBUtil


class BookingSystemRepositoryImpl(IBookingSystemRepository):
    def __init__(self):
        self.conn = DBUtil.get_db_conn()
        self.cursor = self.conn.cursor()

    def create_event(self, event):
        sql = "INSERT INTO event (event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (event.event_name, event.event_date, event.event_time, event.venue.venue_id, event.total_seats,
               event.available_seats, event.ticket_price, event.event_type)
        self.cursor.execute(sql, val)
        self.conn.commit()
        print("Event added to DB.")

    def get_event_details(self):
        self.cursor.execute("SELECT * FROM event")
        return self.cursor.fetchall()

    def get_available_no_of_tickets(self):
        self.cursor.execute("SELECT SUM(available_seats) FROM event")
        result = self.cursor.fetchone()
        return result[0]

    def calculate_booking_cost(self, num_tickets, price):
        return num_tickets * price

    def book_tickets(self, event_name, num_tickets, customers):
        self.cursor.execute("SELECT event_id, available_seats, ticket_price FROM event WHERE event_name = %s",
                            (event_name,))
        event = self.cursor.fetchone()
        if not event:
            raise Exception("Event not found")
        event_id, available, price = event
        if available < num_tickets:
            raise Exception("Not enough tickets")
        total = num_tickets * price

        # Insert each customer and the booking
        for customer in customers:
            self.cursor.execute("INSERT INTO customer (customer_name, email, phone_number) VALUES (%s, %s, %s)",
                                (customer.customer_name, customer.email, customer.phone_number))
            customer_id = self.cursor.lastrowid
            self.cursor.execute(
                "INSERT INTO booking (customer_id, event_id, num_tickets, total_cost, booking_date) VALUES (%s, %s, %s, %s, CURDATE())",
                (customer_id, event_id, 1, price))  # 1 ticket per customer

        # Update availability
        self.cursor.execute("UPDATE event SET available_seats = available_seats - %s WHERE event_id = %s",
                            (num_tickets, event_id))
        self.conn.commit()

    def cancel_booking(self, booking_id):
        self.cursor.execute("SELECT num_tickets, event_id FROM booking WHERE booking_id = %s", (booking_id,))
        booking = self.cursor.fetchone()
        if not booking:
            raise Exception("Invalid booking ID")
        tickets, event_id = booking
        self.cursor.execute("DELETE FROM booking WHERE booking_id = %s", (booking_id,))
        self.cursor.execute("UPDATE event SET available_seats = available_seats + %s WHERE event_id = %s",
                            (tickets, event_id))
        self.conn.commit()

    def get_booking_details(self, booking_id):
        self.cursor.execute("SELECT * FROM booking WHERE booking_id = %s", (booking_id,))
        return self.cursor.fetchone()
