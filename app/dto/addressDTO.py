from pydantic import BaseModel


class CreateAddressDTO(BaseModel):
    street: str
    number: str
    city: str
    state: str
    country: str
    zip_code: str
    latitude: float
    longitude: float

    class Config:
        from_attributes = True



class AddressDTO(BaseModel):
    id: int
    street: str
    number: str
    city: str
    state: str
    country: str
    zip_code: str
    latitude: float
    longitude: float

    class Config:
        from_attributes = True



