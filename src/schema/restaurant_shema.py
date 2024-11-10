from pydantic import BaseModel


class RestaurantCreate(BaseModel):
    name: str
    owner_id: int

class RestaurantUpdate(BaseModel):
    name: str
    owner_id: int