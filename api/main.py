from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.logic import TaskManager

app = FastAPI(title="Restaurant Reservation API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

task_mgr = TaskManager()

# Models aligned with DB and code
class UserCreate(BaseModel):
    name: str
    email: str
    phone_number: str

class TableCreate(BaseModel):
    table_number: int
    capacity: int
    location: str
    status: str = "Available"

class ReservationCreate(BaseModel):
    user_id: int
    table_id: int
    reservation_date: str
    reservation_time: str
    number_of_people: int
    special_request: str | None = None

@app.post("/users")
def create_user(user: UserCreate):
    return task_mgr.register_user(user.name, user.email, user.phone_number)

@app.get("/users")
def list_users():
    return task_mgr.get_users()

@app.post("/tables")
def create_table(table: TableCreate):
    return task_mgr.add_table(table.table_number, table.capacity, table.location, table.status)

@app.get("/tables")
def list_tables():
    return task_mgr.get_tables()

@app.get("/tables/available")
def get_available_tables():
    return task_mgr.get_available_tables()

@app.post("/reservations")
def create_reservation(reservation: ReservationCreate):
    return task_mgr.make_reservation(
        reservation.user_id,
        reservation.table_id,
        reservation.reservation_date,
        reservation.reservation_time,
        reservation.number_of_people,
        reservation.special_request
    )

@app.get("/reservations")
def list_reservations():
    return task_mgr.get_reservations()

@app.get("/reservations/user/{user_id}")
def reservations_by_user(user_id: int):
    return task_mgr.get_reservations_by_user(user_id)

@app.delete("/reservations/{reservation_id}")
def cancel_reservation(reservation_id: int):
    result = task_mgr.cancel_reservation(reservation_id)
    if result.get("success"):
        return {"success": True, "message": "Reservation cancelled successfully"}
    else:
        raise HTTPException(status_code=400, detail=result.get("error", "Unable to cancel reservation"))
