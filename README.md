# Transport Service Booking System

This project is a Command-Line Interface (CLI) Python application designed to simulate a basic transport ticketing system. It allows users to create an account, log in securely, and manage their travel itineraries by booking, viewing, and canceling tickets for buses or trains.

## 🚀 Features

### User Authentication
* **User Registration (`registration`):** Allows new users to create an account by providing a unique username and a strong password. The system checks if the username already exists to prevent duplicates.
* **User Login (`login`):** Validates registered credentials. Upon successful authentication, the user is granted access to the booking dashboard.

### Ticket Management Dashboard
* **Book Ticket (`Ticket_booking`):** Users can book a journey by entering passenger details (Name, Email), Destination, Mode of Transport (Train/Bus), and assigning a custom integer Ticket ID.
* **View Ticket (`show_ticket`):** Retrieves and displays the full itinerary and passenger details using the unique Ticket ID.
* **Cancel Ticket (`Ticket_cancel`):** Allows users to delete a booked ticket from the system using their Ticket ID, featuring a simulated refund confirmation message.

## 🧠 Code Architecture & Data Flow

This application is built using fundamental Python concepts, making it entirely self-contained without the need for external databases or third-party libraries. 

### Data Storage (In-Memory)
The system uses two global dictionaries to store data temporarily while the script is running:
* `users = {}`: Acts as the user database. The username serves as the key, and the password serves as the value (`{user_name: password}`).
* `Ticket = {}`: Acts as the booking database. The integer `Ticket_id` serves as the key, and the value is a nested dictionary containing all passenger and journey details.

### Function Breakdown
1. **`registration()`:** Prompts for credentials, checks for existing keys in the `users` dictionary, and saves the new user.
2. **`login()`:** Verifies if the entered username exists and if the provided password matches the stored value. Grants access to `options()` upon success.
3. **`options()`:** The main routing menu for authenticated users, utilizing conditional statements (`if/elif/else`) to direct the user to booking, viewing, or canceling functions.
4. **`Ticket_booking()`:** Collects 5 distinct data points from the user and constructs a nested dictionary entry within the global `Ticket` dictionary.
5. **`show_ticket()`:** Takes a Ticket ID input, verifies its existence in the `Ticket` dictionary, and prints the formatted values.
6. **`Ticket_cancel()`:** Utilizes the `del` keyword to remove a specific key-value pair from the `Ticket` dictionary.

## 📋 Prerequisites

* **Python 3.x:** Ensure Python is installed on your machine. You can verify this by running `python --version` in your terminal.
* **No external libraries required:** The script uses pure standard Python.

## 🛠️ Installation & Execution

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/chandrahas2007-tech/transport_management]
