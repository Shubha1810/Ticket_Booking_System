
````markdown
# 🎟️ Ticket Booking System

A **Python-based Command-Line Interface (CLI)** application for managing events and ticket bookings. Built for simplified event handling and ticketing operations, this system allows organizers and users to:

- Create and manage events
- Book and cancel tickets
- View and filter bookings by date, month, and year
- Get clean tabular outputs using `tabulate`

---

## 🗂️ Project Structure

```plaintext
ticket_booking_system/
│
├── main.py                              # Main CLI-based entry point
│
├── services/                            # Core business logic
│   └── ticket_booking_system.py
│
├── entity/                              # Data model classes
│   └── customer.py
│
├── exception/                           # Custom exception handling
│   ├── event_not_found_exception.py
│   └── invalid_booking_id_exception.py
│
└── util/                                # Optional helper utilities (if any)
````

### 🗃️ MySQL Integration & Tasks

This project also includes **SQL task files** that demonstrate database setup and query operations using **MySQL**.

#### 📦 Breakdown of SQL Tasks:

| Task       | Description                               | File(s)                                    |
| ---------- | ----------------------------------------- | ------------------------------------------ |
| **Task 1** | Table creation & data insertion           | `created_table.sql`, `inserted_values.sql` |
| **Task 2** | Query operations (e.g., SELECT, JOIN)     | `Task2.sql`                                |
| **Task 3** | Advanced queries (e.g., GROUP BY, HAVING) | `Task3.sql`                                |
| **Task 4** | Aggregation, filtering, subqueries        | `Task4.sql`                                |

#### ✅ Usage:

To execute any SQL task, open your MySQL CLI or GUI (e.g., MySQL Workbench) and run:

```sql
SOURCE path/to/created_table.sql;
SOURCE path/to/inserted_values.sql;
-- Then run other tasks like:
SOURCE path/to/Task2.sql;
```


## 🔄 Major Functional Flow

### 1️⃣ Event Creation

* Inputs Required:

  * Event Name (minimum 3 characters)
  * Date (optional, defaults to today)
  * Time (HH\:MM format)
  * Total Seats (positive integer)
  * Ticket Price (positive number)
  * Event Type (Movie/Concert/Sports)
  * Venue City & Address

✅ Returns a system-generated Event ID upon successful creation.

---

### 2️⃣ Ticket Booking

* Lists all available events
* User selects event by index
* Inputs:

  * Number of tickets
  * For each ticket:

    * Name (minimum 3 chars)
    * Email (must end with `@gmail.com`)
    * Phone (10 digits)

✅ Successful booking shows:

* Booking ID
* Event Details
* Total Cost
* Booking Date
* Customer Info in tabular format

---

### 3️⃣ Cancel Booking

* Input: Booking ID
* Booking is removed if ID is valid
* Handles invalid IDs using custom exceptions

---

### 4️⃣ View Bookings

Filter options:

* View All Bookings
* View by Date Range
* View by Month (MM)
* View by Year (YYYY)

🔎 Displays tabular booking info with:

* Booking ID
* Event Name
* Number of Tickets
* Total Cost
* Booking Date

---

## 🧪 Sample Output

```bash
+-------------+-----------------+----------+--------+------------+
| Booking ID  | Event           | Tickets  | Cost   | Date       |
+-------------+-----------------+----------+--------+------------+
| 101         | Coldplay Live   | 3        | ₹4500  | 2025-07-01 |
+-------------+-----------------+----------+--------+------------+
```

---

## 🧾 Input Validations

| Field       | Rule                                    |
| ----------- | --------------------------------------- |
| Name        | Minimum 3 characters, only alphabets    |
| Email       | Must end with `@gmail.com`              |
| Phone       | Exactly 10 digits                       |
| Date        | Must follow `YYYY-MM-DD` format         |
| Event Type  | Must be `movie`, `concert`, or `sports` |
| Seats/Price | Must be positive integers/floats        |

---

## ⚙️ Tech Stack

| Component             | Description                                |
| --------------------- | ------------------------------------------ |
| **Python 3.x**        | Core language                              |
| **tabulate**          | For displaying clean CLI tables            |
| **datetime**          | Handling event and booking dates           |
| **Custom Exceptions** | For handling invalid operations gracefully |

---

## ▶️ How to Run

### 🔌 Prerequisites

* Python 3.x installed
* Terminal or command prompt

### 🛠️ Installation

Install the required Python library:

```bash
pip install tabulate
```

### 🚀 Run the App

```bash
python main.py
```

---

## 🧭 Sample Workflow

1. 🎭 Create an Event (e.g., Coldplay Concert in Mumbai)
2. 👥 Book 2-3 tickets using user details
3. 🔍 View all bookings or filter by month/year
4. ❌ Cancel a booking using Booking ID
5. 📊 Generate a report-like view from bookings

---

## ❗ Error Handling & Exceptions

| Scenario                    | Handling Mechanism                 |
| --------------------------- | ---------------------------------- |
| Invalid Event Selection     | Graceful message with retry option |
| Booking with Wrong Inputs   | Input validations & error messages |
| Cancel Non-existent Booking | `InvalidBookingIDException` raised |
| Event Not Found             | `EventNotFoundException` raised    |

---

## 📈 Use Case Scenarios

| 🎯 Role         | 🔍 Purpose                         |
| --------------- | ---------------------------------- |
| Event Organizer | Add and manage events              |
| Customer/User   | Book tickets and view events       |
| Admin Operator  | View reports on bookings over time |

---

## 💡 Future Enhancements

* 🌐 Web-based version using Flask/Django
* 📤 Export bookings to Excel/CSV
* 🔐 Admin login & role-based access
* 🧾 QR code generation for booked tickets
* 📱 SMS/email notifications

---

