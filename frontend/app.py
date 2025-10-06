import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Restaurant Reservation System", layout="centered")
st.title("🍽 Restaurant Reservation System")

menu = st.sidebar.radio("Navigation", ["Users", "Tables", "Reservations"])

# USERS
if menu == "Users":
    st.header("👤 Manage Users")
    with st.form("create_user"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone_number = st.text_input("Phone Number")
        if st.form_submit_button("Create User"):
            res = requests.post(f"{API_URL}/users", json={"name": name, "email": email, "phone_number": phone_number})
            st.json(res.json())
    if st.button("View All Users"):
        st.json(requests.get(f"{API_URL}/users").json())

# TABLES
elif menu == "Tables":
    st.header("🪑 Manage Tables")
    with st.form("create_table"):
        table_number = st.number_input("Table Number", min_value=1, step=1)
        capacity = st.number_input("Capacity", min_value=1, step=1)
        location = st.text_input("Location (optional)")
        status = st.selectbox("Status", ["Available", "Occupied"])
        if st.form_submit_button("Create Table"):
            res = requests.post(f"{API_URL}/tables", json={
                "table_number": table_number, "capacity": capacity, "location": location, "status": status
            })
            st.json(res.json())
    if st.button("View All Tables"):
        st.json(requests.get(f"{API_URL}/tables").json())
    if st.button("View Available Tables"):
        st.json(requests.get(f"{API_URL}/tables/available").json())

# RESERVATIONS
elif menu == "Reservations":
    st.header("📅 Manage Reservations")
    with st.form("create_reservation"):
        user_id = st.number_input("User ID", min_value=1, step=1)
        table_id = st.number_input("Table ID", min_value=1, step=1)
        reservation_date = st.date_input("Reservation Date")
        reservation_time = st.time_input("Reservation Time")
        number_of_people = st.number_input("Number of People", min_value=1, step=1)
        special_request = st.text_area("Special Request (optional)")
        if st.form_submit_button("Create Reservation"):
            res = requests.post(f"{API_URL}/reservations", json={
                "user_id": user_id, "table_id": table_id,
                "reservation_date": str(reservation_date),
                "reservation_time": str(reservation_time),
                "number_of_people": number_of_people,
                "special_request": special_request
            })
            st.json(res.json())
    user_lookup = st.number_input("Lookup Reservations (User ID)", min_value=1, step=1, key="lookup")
    if st.button("View User Reservations"):
        st.json(requests.get(f"{API_URL}/reservations/user/{user_lookup}").json())
    if st.button("View All Reservations"):
        st.json(requests.get(f"{API_URL}/reservations").json())
    cancel_id = st.number_input("Cancel Reservation ID", min_value=1, step=1, key="cancel")
    if st.button("Cancel Reservation"):
        res = requests.delete(f"{API_URL}/reservations/{cancel_id}")
        st.json(res.json())
