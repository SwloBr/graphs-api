from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Relationship

from app.database import Base


class Address(Base):
    __tablename__ = "address"

    id = Column("id", Integer, primary_key=True, index=True, autoincrement=True)
    street = Column("street", String, index=True, nullable=True)
    number = Column("number", String, index=True, nullable=False)
    city = Column("city", String, index=True, nullable=False)
    state = Column("state", String, index=True, nullable=False, default="GO")
    country = Column("country", String, index=True, nullable=False, default="Brazil")
    zip_code = Column("zip_code", String, index=True, nullable=False)
    latitude = Column("latitude", String, index=True, nullable=True)
    longitude = Column("longitude", String, index=True, nullable=True)

    industry = Relationship("Industry", back_populates="address")
