from sqlalchemy.orm import Session

from app.models import Fuel


class FuelRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_fuel_by_id(self, fuel_id: int):
        return self.db.query(Fuel).filter(fuel_id == Fuel.id).first()

    def get_fuel_by_type(self, fuel_type: str):
        return self.db.query(Fuel).filter(fuel_type == Fuel.type).first()

    def create_fuel(self, fuel: Fuel):
        self.db.add(fuel)
        self.db.commit()
        self.db.refresh(fuel)
        return fuel

    def update_fuel(self, fuel: Fuel, **fields):
        for key, value in fields.items():
            setattr(fuel, key, value)
        self.db.commit()
        self.db.refresh(fuel)
        return fuel

    def delete_fuel(self, fuel: Fuel):
        self.db.delete(fuel)
        self.db.commit()
        return fuel

    def get_all_fuels(self):
        return self.db.query(Fuel).all()
