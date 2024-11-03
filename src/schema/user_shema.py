from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    phone: str

class UserUpdate(BaseModel):
    name: str
    phone: str

class RestaurantCreate(BaseModel):
    name: str
    owner_id: int

class RestaurantUpdate(BaseModel):
    name: str
    owner_id: int
