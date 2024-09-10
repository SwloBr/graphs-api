from app.database import get_db
from app.models import Address
from app.repositories import AddressRepository


class AddressService:
    def __init__(self, db=None):
        self.db = db if db is not None else next(get_db())
        self.address_repository = AddressRepository(self.db)

    def get_address(self, address_id):
        return self.address_repository.get_address_by_id(address_id)

    def create_address(self, raw_address):

        address = Address(**raw_address.dict())

        return self.address_repository.create_address(address)

    def update_address(self, address):
        return self.address_repository.update_address(address)

    def delete_address(self, address_id):
        return self.address_repository.delete_address(address_id)

    def get_all_addresses(self):
        return self.address_repository.get_all_addresses()