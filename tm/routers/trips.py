from fastapi import APIRouter, HTTPException
from schemas.trip_service import trip_service, TripService
from datetime import date

router = APIRouter(prefix="/trips", tags=["Trips"])

@router.post("/schedule")
def schedule_trip(vehicle_id: int, route_id: int, departure_date: date, arrival_date: date, trip_type: str, max_passengers: int):
    if departure_date <= date.today() or arrival_date <= date.today():
        raise HTTPException(status_code=400, detail="Departure and arrival dates must be in the future.")
    success = TripService.schedule_trip(vehicle_id, route_id, departure_date, arrival_date, trip_type, max_passengers)
    if success:
        return {"message": "Trip scheduled successfully!"}
    else:
        raise HTTPException(status_code=400, detail="Failed to schedule trip.")



@router.delete("/cancel/{trip_id}")
def cancel_trip(trip_id: int):
    success = TripService.cancel_trip(trip_id)
    if success:
        return {"message": "Trip canceled successfully!"}
    else:
        raise HTTPException(status_code=404, detail="Trip not found or unable to cancel.")