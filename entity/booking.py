from datetime import datetime

class Booking:
    booking_counter = 1

    def __init__(self, customers, event, num_tickets, total_cost=None, booking_date=None):
        self.booking_id = Booking.booking_counter
        Booking.booking_counter += 1

        self.customers = customers
        self.event = event
        self.num_tickets = num_tickets
        self.total_cost = total_cost if total_cost is not None else num_tickets * event.ticket_price
        self.booking_date = booking_date if booking_date else datetime.now()

    def display_booking_details(self):
        print(f"\nBooking ID: {self.booking_id}")
        print(f"Event: {self.event.event_name}")
        print(f"Tickets: {self.num_tickets} | Total Cost: ₹{self.total_cost}")
        print(f"Booking Time: {self.booking_date}")
        print("Customer Details:")
        for c in self.customers:
            print(f"{c.customer_name} | {c.email} | {c.phone_number}")
