#db manager.py
import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")

SUPABASE=create_client(url,key)

# =============== user table ========#
#Add user
def add_user(name,email,phoneno):
    return SUPABASE.table("users").insert(
        {
            "name":name,
            "email":email,
            "phoneno":phoneno
        }
    ).execute()

#get users
def get_user():
    return SUPABASE.table("users").select("*").execute()

#get_user_by_id
def get_user_by_id(user_id):
    return SUPABASE.table("users").select("*").eq("user_id",user_id).execute()

# =========Table table ============#

#Add table

def add_table(table_number,capacity,location,status="Available"):
    return SUPABASE.table("restaurant_tables").insert(
        {
            "table_number":table_number,
            "capacity":capacity,
            "location":location,
            "status":status
        }
    ).execute()

#get tables
def get_tables():
    return SUPABASE.table("restaurant_tables").select("*").execute()

#def update table status

def update_table_status(table_id,status):
    return SUPABASE.table("restaurant_tables").update({"status": status}).eq("table_id",table_id).execute()

#============reservation status===========#

def add_reservation_status(user_id: int, table_id: int, reservation_date: str, reservation_time: str, number_of_people: int, special_request: str = None):
    return SUPABASE.table("reservations").insert(
        {
            "user id":user_id,
            "table id":table_id,
            "reservation date":reservation_date,
            "reservation time":reservation_time,
            "number of people":number_of_people,
            "special_request":special_request
        }
    ).execute()

#=============get reservations ==============#
def get_reservations():
    return SUPABASE.table("reservations").select("*").execute()

#=============get reservations by user===========#
def get_reservation_by_user(user_id):
    return SUPABASE.table("reservations").select("*").eq("user id",user_id).execute()

#=============cancel reservations===============#
def cancel_reservation(reservation_id: int):
    return SUPABASE.table("reservations").update({"status": "Cancelled"}).eq("reservation_id", reservation_id).execute()