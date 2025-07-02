
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

- 🎫 Create Events (Movies, Concerts, Sports)
- 👁️ View Event Listings
- 👥 Book Tickets for Multiple Customers
- ❌ Cancel Existing Bookings
- 📆 View Bookings (All, Date Range, Month, Year-wise)
- 🔒 Validations for Name, Email, Phone, Dates
- 📊 Clean output using `tabulate`

---

## 🛠️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/YourUsername/Ticket_Booking_System.git
cd Ticket_Booking_System
````

2. **Install Dependencies**

```bash
pip install tabulate
```

3. **Run the Application**

```bash
python main.py
```

---

## 🔄 Application Flow

### 1. Main Menu Options

* Create Event
* View Event Details
* Book Tickets
* Cancel Booking
* View Bookings by Date/Month/Year
* Exit

---

### 2. Create Event

Inputs required:

* Event Name (minimum 3 letters)
* Date (optional — defaults to today)
* Time (HH\:MM format)
* Total Seats (positive integer)
* Ticket Price (positive number)
* Event Type (Movie/Concert/Sports)
* Venue City & Address

🆗 Successful creation returns a unique Event ID.

---

### 3. View Event Details

Shows a formatted table listing:

* Event Name
* Time
* Venue
* Ticket Price

---

### 4. Book Tickets

* Choose event from the list
* Enter number of tickets
* For each ticket:

  * Name (validated)
  * Email (must be `@gmail.com`)
  * Phone (10 digits)

🎉 Booking Confirmation:

* Booking ID
* Event Name
* Total Cost
* Booking Time
* Customer list in table format

---

### 5. Cancel Booking

* Input booking ID
* System cancels the booking and updates availability
* Handles invalid booking IDs using custom exceptions

---

### 6. View Bookings

Filter options:

* All Bookings
* Date Range (YYYY-MM-DD)
* Month (MM)
* Year (YYYY)

Shows a table of:

* Booking ID
* Event Name
* Tickets
* Total Cost
* Booking Date

---

## 🧪 Input Validations

| Field       | Rule                                |
| ----------- | ----------------------------------- |
| Name        | At least 3 characters, only letters |
| Email       | Must end with `@gmail.com`          |
| Phone       | Exactly 10 digits                   |
| Date        | Format `YYYY-MM-DD`                 |
| Event Type  | Must be Movie, Concert, or Sports   |
| Seats/Price | Positive numbers only               |

---

## 📦 Libraries Used

* `tabulate` – for clean and formatted table outputs
* `datetime` – for date/time parsing and filtering
* Custom Exceptions – for handling edge cases smoothly

---

## 👀 Sample Output

```
--- Ticket Booking Menu ---
1. Create Event
2. View Event Details
3. Book Tickets
4. Cancel Booking
5. View Bookings by Date/Month/Year
6. Exit
```

---
