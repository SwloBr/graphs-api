from app.database import get_db
from app.models import Truck
from app.repositories import TruckRepository


class TruckService:
    def __init__(self, db=None):
        self.db = db if db is not None else next(get_db())
        self.truck_repository = TruckRepository(self.db)

    def get_truck_by_id(self, truck_id):
        return self.truck_repository.get_truck_by_id(truck_id)

    def get_truck_by_name(self, truck_id):
        return self.truck_repository.get_truck_by_name(truck_id)

    def get_trucks(self):
        return self.truck_repository.get_all_trucks()

    def create_truck(self, raw_truck):

        truck = Truck(**raw_truck.dict())
        return self.truck_repository.create_truck(truck)

    def update_truck(self, truck):
        self.truck_repository.update_truck(truck)

    def delete_truck(self, truck_id):
        self.truck_repository.delete_truck(truck_id)