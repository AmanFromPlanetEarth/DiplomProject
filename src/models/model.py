from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Model(DeclarativeBase):
    pass

class UserModel(Model):
    __tablename__="users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    phone: Mapped[str] = mapped_column(String(13))
    #restaurants = relationship("RestaurantModel", back_populates="owner")
    

class RestaurantModel(Model):
    __tablename__ = "restaurants"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("UserModel.id"))
    #owner = relationship("UserModel", back_populates="restaurants")