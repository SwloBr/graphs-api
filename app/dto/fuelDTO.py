from pydantic import BaseModel


class FuelDTO(BaseModel):
    id: int
    type: str
    price: float

    class Config:
        from_attributes = True


class CreateFuelDTO(BaseModel):
    type: str
    price: float

    class Config:
        from_attributes = True
