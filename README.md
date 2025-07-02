
```markdown
# 🎟️ Ticket Booking System

A console-based Python application to manage events and ticket bookings. Users can create events, book or cancel tickets, and view booking reports by date, month, or year.

---

## 📁 Project Structure

```

ticket\_booking\_system/
│
├── main.py                              # Main script with user interaction menu
├── services/
│   └── ticket\_booking\_system.py         # Business logic for booking system
├── entity/
│   └── customer.py                      # Customer class with name, email, phone
├── exception/
│   ├── event\_not\_found\_exception.py     # Custom exception for missing events
│   └── invalid\_booking\_id\_exception.py  # Custom exception for invalid bookings
└── util/
└── (optional helper utils if used)

````

---

## 🚀 Features

- Create Events (Movies, Concerts, Sports)
- View Event Listings
- Book Tickets for Multiple Customers
- Cancel Existing Bookings
- View Bookings (All, Date Range, Month, Year-wise)
- Validations for Name, Email, Phone, Dates
- Formatted table output using `tabulate`

---

## 🛠️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/YourUsername/Ticket_Booking_System.git
cd Ticket_Booking_System
````

2. **Install Dependencies**

This project uses the `tabulate` library:

```bash
pip install tabulate
```

3. **Run the Application**

```bash
python main.py
```

## 🔄 Application Flow

### 1. **Main Menu**

User is presented with 6 options:

* Create Event
* View Event Details
* Book Tickets
* Cancel Booking
* View Bookings
* Exit


### 2. **Create Event**

User provides:

* Event Name (validated)
* Date (optional: uses today if empty)
* Time
* Total Seats
* Ticket Price
* Event Type (`Movie`, `Concert`, `Sports`)
* Venue and Address

✅ Event gets added to the system with a unique event ID.


### 3. **View Event Details**

Displays a **tabulated list** of all available events with:

* Name
* Time
* Venue
* Price

### 4. **Book Tickets**

Flow:

1. Lists all events with indexes.
2. User selects an event by number.
3. User enters number of tickets.
4. For each ticket, user enters:

   * Name (validated)
   * Email (must end with `@gmail.com`)
   * Phone (10-digit number)

✅ Booking confirmation is shown with:

* Booking ID
* Event Name
* Total Cost
* Booking Date
* Customer Details in tabular form


### 5. **Cancel Booking**

User enters a booking ID.
If valid, the booking is removed and seats are freed.
Handles invalid ID with custom exceptions.


### 6. **View Bookings**

User can filter bookings by:

* All Bookings
* Date Range
* Month (MM format)
* Year (YYYY format)

Displays bookings in a table with:

* Booking ID
* Event Name
* No. of Tickets
* Total Cost
* Booking Date


## 🧪 Validations

| Field         | Validation                                  |
| ------------- | ------------------------------------------- |
| Name          | At least 3 characters, alphabet only        |
| Email         | Must end with `@gmail.com`                  |
| Phone         | 10 digits only                              |
| Date          | `YYYY-MM-DD` format                         |
| Event Type    | Must be either `movie`, `concert`, `sports` |
| Tickets/Seats | Positive integers only                      |


## 📦 Libraries Used

* `tabulate` - for clean table-based CLI output
* `datetime` - to handle dates and timestamps
* Custom Exceptions for error handling

## 📸 Sample Output

```
--- Ticket Booking Menu ---
1. Create Event
2. View Event Details
3. Book Tickets
4. Cancel Booking
5. View Bookings by Date/Month/Year
6. Exit
```


