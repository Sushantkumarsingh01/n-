from pydantic import BaseModel

from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: str
    username: str
    password: str
    role: str
