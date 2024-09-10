from pydantic import BaseModel


class TruckDTO(BaseModel):
    id: int
    name: str
    max_tons: int
    axles: int
    km_per_fuel: float
    fuel_id: int

    class Config:
        from_attributes = True


class CreateTruckDTO(BaseModel):
    name: str
    max_tons: int
    axles: int
    km_per_fuel: float
    fuel_id: int

    class Config:
        from_attributes = True
