from fastapi import APIRouter
from schemas.driver_service import DriverService

router = APIRouter(prefix="/drivers", tags=["Drivers"])

@router.get("/available")
def get_available_drivers():
    drivers = DriverService.get_available_drivers()
    return {"drivers": drivers}
