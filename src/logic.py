# managers.py

from src.db import DatabaseManager

# ---------------- USER MANAGER ----------------
class UserManager:
    """
    Handles all user-related operations.
    """
    def __init__(self):
        self.db = DatabaseManager()

    def register_user(self, name: str, email: str, phone_no: str):
        if not name or not phone_no:
            return {"success": False, "message": "Name & Phone number are required"}

        result = self.db.add_user(name, email, phone_no)
        if result.get("success"):
            return {"success": True, "message": "User added successfully"}
        else:
            return {"success": False, "message": f"Error: {result.get('error')}"}

    def get_users(self):
        return self.db.get_users()

    def get_user_by_id(self, user_id: int):
        return self.db.get_user_by_id(user_id)


# ---------------- TABLE MANAGER ----------------
class TableManager:
    """
    Handles all restaurant table operations.
    """
    def __init__(self):
        self.db = DatabaseManager()

    def add_table(self, table_number: int, capacity: int, status: str = "Available"):
        result = self.db.add_table(table_number, capacity, status)
        if result.get("success"):
            return {"success": True, "message": "Table added successfully"}
        else:
            return {"success": False, "message": f"Error: {result.get('error')}"}

    def get_tables(self):
        return self.db.get_tables()

    def get_available_tables(self):
        tables = self.db.get_tables()
        if not tables.get("success"):
            return tables
        available = [t for t in tables["data"] if t["status"] == "Available"]
        return {"success": True, "data": available}

    def update_table_status(self, table_id: int, status: str):
        return self.db.update_table_status(table_id, status)


# ---------------- RESERVATION MANAGER ----------------
class ReservationManager:
    """
    Handles all reservation-related operations.
    """
    def __init__(self):
        self.db = DatabaseManager()
        self.table_manager = TableManager()  # To update table status

    def make_reservation(self, user_id: int, table_id: int, reservation_date: str,
                         reservation_time: str, number_of_people: int, special_request: str = None):
        # Check table availability
        available = self.table_manager.get_available_tables()
        if not available.get("success"):
            return available
        if not any(t["table_id"] == table_id for t in available["data"]):
            return {"success": False, "message": "Table not available"}

        # Add reservation
        result = self.db.add_reservation(
            user_id, table_id, reservation_date, reservation_time,
            number_of_people, special_request
        )

        if result.get("success"):
            # Mark table as reserved
            self.table_manager.update_table_status(table_id, "Reserved")
            return {"success": True, "message": "Reservation created successfully"}
        else:
            return {"success": False, "message": f"Error: {result.get('error')}"}

    def get_reservations_by_user(self, user_id: int):
        return self.db.get_reservations_by_user(user_id)

    def get_all_reservations(self):
        return self.db.get_all_reservations()

    def cancel_reservation(self, reservation_id: int, table_id: int):
        result = self.db.cancel_reservation(reservation_id)
        if result.get("success"):
            self.table_manager.update_table_status(table_id, "Available")
            return {"success": True, "message": "Reservation cancelled"}
        else:
            return {"success": False, "message": f"Error: {result.get('error')}"}
