from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys, os

# Add src directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.managers import UserManager, TableManager, ReservationManager

# ----------------------------------- App Setup ----------------------
app = FastAPI(title="Restaurant Reservation API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow_origins 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------- Instances ----------------------
user_mgr = UserManager()
table_mgr = TableManager()
res_mgr = ReservationManager()


class UserCreate(BaseModel):
    name: str
    email: str
    phone_no: str

class TableCreate(BaseModel):
    table_number: int
    capacity: int
    status: str = "Available"

class ReservationCreate(BaseModel):
    user_id: int
    table_id: int
    reservation_date: str  # YYYY-MM-DD
    reservation_time: str  # HH:MM
    number_of_people: int
    special_request: str = None

# ----------------------------------- Routes --------------------------

# ---------- User Routes ----------
@app.post("/users")
def create_user(user: UserCreate):
    return user_mgr.register_user(user.name, user.email, user.phone_no)

@app.get("/users")
def list_users():
    return user_mgr.get_users()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return user_mgr.get_user_by_id(user_id)


# ---------- Table Routes ----------
@app.post("/tables")
def create_table(table: TableCreate):
    return table_mgr.add_table(table.table_number, table.capacity, table.status)

@app.get("/tables")
def list_tables():
    return table_mgr.get_tables()

@app.get("/tables/available")
def list_available_tables():
    return table_mgr.get_available_tables()


# ---------- Reservation Routes ----------
@app.post("/reservations")
def create_reservation(reservation: ReservationCreate):
    return res_mgr.make_reservation(
        reservation.user_id,
        reservation.table_id,
        reservation.reservation_date,
        reservation.reservation_time,
        reservation.number_of_people,
        reservation.special_request
    )

@app.get("/reservations/user/{user_id}")
def user_reservations(user_id: int):
    return res_mgr.get_reservations_by_user(user_id)

@app.get("/reservations")
def all_reservations():
    return res_mgr.get_all_reservations()

@app.delete("/reservations/{reservation_id}/table/{table_id}")
def cancel_reservation(reservation_id: int, table_id: int):
    return res_mgr.cancel_reservation(reservation_id, table_id)

if __name__=="main":
    import uvicorn
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)