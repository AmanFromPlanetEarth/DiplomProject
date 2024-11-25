from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str

class UserUpdate(BaseModel):
    name: str
    email: EmailStr
    phone: str


