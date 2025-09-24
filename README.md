# Restaurant Reservation System

The Restaurant Table Reservation System is a software application designed to automate and streamline the process of booking tables in a restaurant. The system allows customers to reserve tables in advance, manage their bookings, and receive confirmation, while enabling restaurant staff to efficiently handle table availability, reservations, and customer preferences.

This system reduces manual effort, avoids double bookings, minimizes waiting times, and enhances the overall customer experience. It can be implemented as a web application, desktop application, or mobile app, depending on the project requirements.

# Features
Book tables by selecting date, time, and number of guests.

View real-time table availability.

Receive booking confirmations via email, SMS, or app notifications.

Modify or cancel reservations.

Specify special requests (window seat, celebrations, etc.).

View booking history for easy rebooking.

Add, update, or cancel reservations.

Manage table details (availability, capacity, status).

Maintain waitlists when tables are fully booked.

Access customer details and booking history.

Generate reports on bookings, peak hours, and occupancy.

Receive notifications about new or canceled reservations.


## project structure

Restaurant management 
|
|----src/               # core application  logic
|     |____logic.py      # business logic and task
operations
|     |____db.py         # Data base operations
|
|---api/                # backend api
|    |___main.py        #FastAPI endpoints
|
|---frontend/           # Frontend application
|      |___app.py       #Streamlit web interface
|
|____requirements.txt   #python dependenices
|
|____README.md          #project Documentation
|
|____.env    #python variables

## Quick Start

## Prerequisites

-Python 3.8 or higher
-A Supabase account
-Git(Push,cloning)

### 1.Clone or Download the Project
# Option 1.Clone with Git
git clone<Repository-url>

# Option 2: Download and extract the ZIP file

### 2. Install Dependencies

# Install all required python packages
pip install -r requirements.txt

### 3.Set Up Supabase Database

1.Create a supabase Project:

2.Create the Tasks Table:

- Go to the SQL Editor in your Supabase Dashboard
- Run this SQL command

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(15) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE restaurant_tables (
    table_id SERIAL PRIMARY KEY,
    table_number VARCHAR(10) NOT NULL,
    capacity INT NOT NULL,
    location VARCHAR(50),
    status VARCHAR(20) DEFAULT 'Available'
);


CREATE TABLE reservations (
    reservation_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    table_id INT NOT NULL,
    reservation_date DATE NOT NULL,
    reservation_time TIME NOT NULL,
    number_of_people INT NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending',
    special_request VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_user FOREIGN KEY (user_id)
        REFERENCES users(user_id) ON DELETE CASCADE,
    CONSTRAINT fk_table FOREIGN KEY (table_id)
        REFERENCES restaurant_tables(table_id) ON DELETE CASCADE,
    CONSTRAINT unique_table_booking UNIQUE (table_id, reservation_date, reservation_time)
);


3.Get your Credentials:

## 4.Configure Environmental variables

1.Create a `.env` file in the project root

2.Add your Supabase credentials to `.env`:
  SUPABASE_URL="YOUR_PROJECT_URL"
  SUPABASE_KEY="YOUR_PROJECT_KEY"

  ** EXAMPLE **
  SUPABASE_URL="https://fdpvyjixwktgakxajbra.supabase.co"
  SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZkcHZ5aml4d2t0Z2FreGFqYnJhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODIzNDYsImV4cCI6MjA3MzY1ODM0Nn0.I48KVU9VWay848VXJfSlLABVnmT0elCzBOgIMrJJTjk"

  ### 5.RUN THE APPLICATION

  ## Streamlit Frontend

  Streamlit run frontend/app.py

  the app will open in your browser at `http://localhost:8501`

  ## FastAPI Backend

  cd api
  python main.py

  The API Will be available at  `http://localhost:8000`

  ## How to use

  ## Technical Details

  ## Technologies Used

  **Frontend**:Streamlit (Python web framework)

  **Backend**:FastAPI (Python RESTAPI Framework)

  **Database**:Supabase (PostgreSQL - based backend as a service)

  **Language** :Python 3.8+

  ### Key Components

  1. **`src/db.py`**:Database Operations Handles all CRUD operations with Supabase

  2. **`src/logic.py`**:Business logic task validation and processing 

## Troubleshooting

## Common Issues


## Future Enhancements

## Support

If you encounter any isssues or have any questions:

Contact:9391633764
E-mail:abhimanchukonda@gmail.com


