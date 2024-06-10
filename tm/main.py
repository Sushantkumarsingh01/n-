from fastapi import FastAPI
from routers import users, trips, bookings, drivers

app = FastAPI()

app.include_router(users.router)
app.include_router(trips.router)
app.include_router(bookings.router)
app.include_router(drivers.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Transport Management System API!"}
