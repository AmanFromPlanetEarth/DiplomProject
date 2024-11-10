from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    phone: str

class UserUpdate(BaseModel):
    name: str
    phone: str


