from fastapi import APIRouter, HTTPException
from schemas.booking_service import BookingService
from datetime import date

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.post("/book")
def book_trip(trip_id: int, passenger_id: int, booking_date: date):
    if booking_date <= date.today():
        raise HTTPException(status_code=400, detail="Booking date must be in the future.")
    success = BookingService.book_trip(trip_id, passenger_id, booking_date)
    if success:
        return {"message": "Trip booked successfully!"}
    else:
        raise HTTPException(status_code=400, detail="Failed to book trip.")
