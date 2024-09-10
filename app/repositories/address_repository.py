from sqlalchemy.orm import Session

from app.models import Address


class AddressRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_address_by_id(self, address_id: int):
        return self.db.query(Address).filter(address_id == Address.id).first()

    def create_address(self, address: Address):
        self.db.add(address)
        self.db.commit()
        self.db.refresh(address)
        return address

    def update_address(self, address: Address, **fields):
        for key, value in fields.items():
            setattr(address, key, value)
        self.db.commit()
        self.db.refresh(address)
        return address

    def delete_address(self, address: Address):
        self.db.delete(address)
        self.db.commit()
        return address

    def get_all_addresses(self):
        return self.db.query(Address).all()
