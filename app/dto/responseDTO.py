from pydantic import BaseModel

class ResponseTruckDTO(BaseModel):
    name: str
    max_tons: int
    axles: int
    km_per_fuel: float


class ResponseDTO(BaseModel):
    enterprise: str
    distance: float
    time: float
    cost: float
    earnings: float
    profit: float
    truck: ResponseTruckDTO
