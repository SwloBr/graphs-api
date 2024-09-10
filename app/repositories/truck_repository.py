from sqlalchemy.orm import Session

from app.models import Truck


class TruckRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_truck_by_id(self, truck_id: int):
        return self.db.query(Truck).filter(truck_id == Truck.id).first()

    def get_truck_by_name(self, truck_name: str):
        return self.db.query(Truck).filter(truck_name == Truck.name).first()

    def create_truck(self, truck: Truck):
        self.db.add(truck)
        self.db.commit()
        self.db.refresh(truck)
        return truck

    def update_truck(self, truck: Truck, **fields):
        for key, value in fields.items():
            setattr(truck, key, value)
        self.db.commit()
        self.db.refresh(truck)
        return truck

    def delete_truck(self, truck: Truck):
        self.db.delete(truck)
        self.db.commit()
        return truck

    def get_all_trucks(self):
        return self.db.query(Truck).all()