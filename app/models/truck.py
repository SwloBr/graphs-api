from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import Relationship

from app.database import Base


class Truck(Base):
    __tablename__ = "truck"

    id = Column("id", Integer, primary_key=True, index=True, autoincrement=True)
    name = Column("name", String, index=True, nullable=False, unique=True)
    max_tons = Column("max_tons", Integer, nullable=False, default=1, comment="Maximum tons")
    axles = Column("axles", Integer, nullable=False, default=1, comment="Number of axles")
    km_per_fuel = Column("km_per_fuel", Float, nullable=False, default=1, comment="Kilometers per fuel")
    fuel_id = Column("fuel_id", Integer, ForeignKey('fuel.id'), nullable=False, comment="Fuel type")

    fuel = Relationship("Fuel", back_populates="truck")



