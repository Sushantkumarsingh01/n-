

from fastapi import APIRouter, HTTPException
from schemas.user import User
from schemas.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register")
def register_user(user: User):
    success = UserService.register_user(user)
    if success:
        return {"message": "User registered successfully!"}
    else:
        raise HTTPException(status_code=400, detail="Failed to register user.")

@router.post("/login")
def login_user(username: str, password: str):
    role = UserService.authenticate_user(username, password)
    if role:
        return {"role": role}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password.")
