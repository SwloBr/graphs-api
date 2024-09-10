from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import Relationship

from app.database import Base


class Industry(Base):
    __tablename__ = "industry"

    id = Column("id", Integer, primary_key=True, index=True, autoincrement=True)
    name = Column("name", String, index=True, nullable=False, unique=True)
    address_id = Column("address_id", Integer, ForeignKey('address.id'), nullable=False)
    price = Column("price", Float, nullable=False, default=1, comment="Price per ton")

    address = Relationship("Address", back_populates="industry")
