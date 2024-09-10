from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Relationship

from app.database import Base


class Fuel(Base):
    __tablename__ = "fuel"

    id = Column("id", Integer, primary_key=True, index=True, autoincrement=True)
    type = Column("type", String, index=True, nullable=False, unique=True)
    price = Column("price", Float, nullable=False, default=1, comment="Price per liter")

    truck = Relationship("Truck", back_populates="fuel")