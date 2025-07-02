from services.ticket_booking_system import TicketBookingSystem
from entity.customer import Customer
from exception.event_not_found_exception import EventNotFoundException
from exception.invalid_booking_id_exception import InvalidBookingIDException
from tabulate import tabulate
import re
from datetime import datetime, date


def is_valid_name(name):
    return name and name.strip() and len(name.strip()) >= 3 and name.replace(" ", "").isalpha()


def is_valid_email(email):
    return email.endswith("@gmail.com")


def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10


def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def main():
    system = TicketBookingSystem()

    while True:
        print("\n--- Ticket Booking Menu ---")
        print("1. Create Event")
        print("2. View Event Details")
        print("3. Book Tickets")
        print("4. Cancel Booking")
        print("5. View Bookings by Date/Month/Year")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("Enter Event Name: ").strip()
            if not is_valid_name(name):
                print("Invalid name. Must be at least 3 characters.")
                continue

            date_input = input("Enter Event Date (YYYY-MM-DD): ").strip()

            if not date_input:
                date_str = date.today().strftime("%Y-%m-%d")
                print(f"\U0001F4C5 No date entered. Today's date '{date_str}' will be used as the event date.")
            elif is_valid_date(date_input):
                date_str = date_input
            else:
                print("❌ Invalid date format. Please enter in YYYY-MM-DD.")
                continue

            time = input("Enter Event Time (HH:MM): ")
            if not time.strip():
                print("Time cannot be empty.")
                continue

            try:
                seats = int(input("Enter Total Seats: "))
                if seats <= 0:
                    raise ValueError
            except ValueError:
                print("Total seats must be a positive integer.")
                continue

            try:
                price = float(input("Enter Ticket Price: "))
                if price <= 0:
                    raise ValueError
            except ValueError:
                print("Ticket price must be a positive number.")
                continue

            etype = input("Enter Event Type (Movie/Concert/Sports): ").lower()
            if etype not in ['movie', 'concert', 'sports']:
                print("Invalid event type.")
                continue

            venue = input("Enter Venue City: ").strip()
            address = input("Enter Venue Address: ").strip()

            event_id = system.create_event(name, date_str, time, seats, price, etype, venue, address)
            if event_id:
                print(f" Event created with ID: {event_id}")

        elif choice == '2':
            if not system.events:
                print("No events available.")
            else:
                data = [[ev.event_name, ev.event_time, ev.venue.venue_name, ev.ticket_price] for ev in
                        system.get_sorted_events()]
                print(tabulate(data, headers=["Event Name", "Time", "Venue", "Price"], tablefmt="grid"))

        elif choice == '3':
            if not system.events:
                print("No events to book.")
                continue

            sorted_events = system.get_sorted_events()
            for i, ev in enumerate(sorted_events):
                print(f"{i + 1}. {ev.event_name} ({ev.event_type})")

            user_input = input("Select event number: ")
            if not user_input.isdigit():
                print("Invalid input. Please enter a valid number.")
                continue

            eid = int(user_input) - 1
            if eid < 0 or eid >= len(sorted_events):
                print("Invalid event selection.")
                continue

            try:
                tickets = int(input("Enter number of tickets to book: "))
                if tickets <= 0:
                    raise ValueError
            except ValueError:
                print("Invalid ticket count.")
                continue

            customers = []
            for i in range(tickets):
                print(f"\nCustomer {i + 1} Details:")
                cname = input("Name: ")
                if not is_valid_name(cname):
                    print("Invalid name.")
                    continue

                email = input("Email: ")
                if not is_valid_email(email):
                    print("Invalid email. Must end with @gmail.com")
                    continue

                phone = input("Phone: ")
                if not is_valid_phone(phone):
                    print("Invalid phone number. Must be 10 digits.")
                    continue

                customers.append(Customer(cname, email, phone))

            try:
                booking = system.book_tickets(sorted_events[eid].event_name, tickets, customers)
                if booking:
                    print("Booking successful!")
                    table = [[cust.customer_name, cust.email, cust.phone_number] for cust in booking.customers]
                    print("\nBooking ID:", booking.booking_id)
                    print("Event:", booking.event.event_name)
                    print("Tickets:", booking.num_tickets, "| Total Cost: ₹", booking.total_cost)
                    print("Booking Time:", booking.booking_date)
                    print(tabulate(table, headers=["Name", "Email", "Phone"], tablefmt="grid"))
            except EventNotFoundException as e:
                print(f"Error: {e}")
            except AttributeError:
                print("Unexpected null reference encountered. Please try again.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '4':
            try:
                bid = int(input("Enter Booking ID to cancel: "))
                if system.cancel_tickets(bid):
                    print("Booking cancelled successfully.")
            except InvalidBookingIDException as e:
                print(f"Error: {e}")
            except AttributeError:
                print("Null reference encountered.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '5':
            print("\n1. View All Bookings")
            print("2. Filter by Date Range")
            print("3. Filter by Month")
            print("4. Filter by Year")
            opt = input("Choose filter option: ")
            filtered = []
            if opt == '1':
                filtered = list(system.bookings)
            elif opt == '2':
                start = input("Enter start date (YYYY-MM-DD): ")
                end = input("Enter end date (YYYY-MM-DD): ")
                filtered = [b for b in system.bookings if start <= b.booking_date.strftime("%Y-%m-%d") <= end]
            elif opt == '3':
                month = input("Enter month (MM): ")
                filtered = [b for b in system.bookings if b.booking_date.strftime("%m") == month]
            elif opt == '4':
                year = input("Enter year (YYYY): ")
                filtered = [b for b in system.bookings if b.booking_date.strftime("%Y") == year]

            if filtered:
                table = [
                    [b.booking_id, b.event.event_name, b.num_tickets, b.total_cost, b.booking_date.strftime("%Y-%m-%d")]
                    for b in filtered]
                print(tabulate(table, headers=["Booking ID", "Event", "Tickets", "Cost", "Date"], tablefmt="grid"))
            else:
                print("No bookings found.")

        elif choice == '6':
            print("Thank you for using the Ticket Booking System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
