from app.database import get_db
from app.models import Fuel
from app.repositories import FuelRepository


class FuelService:
    def __init__(self, db=None):
        self.db = db if db is not None else next(get_db())
        self.fuel_repository = FuelRepository(self.db)

    def get_fuel_by_id(self, fuel_id):
        return self.fuel_repository.get_fuel_by_id(fuel_id)

    def get_fuel_by_type(self, fuel_type):
        return self.fuel_repository.get_fuel_by_type(fuel_type)

    def create_fuel(self, raw_fuel):
        fuel = Fuel(**raw_fuel.dict())

        return self.fuel_repository.create_fuel(fuel)

    def update_fuel(self, fuel):
        return self.fuel_repository.update_fuel(fuel)

    def delete_fuel(self, fuel_id):
        return self.fuel_repository.delete_fuel(fuel_id)

    def get_all_fuels(self):
        return self.fuel_repository.get_all_fuels()


