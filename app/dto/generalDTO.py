from pydantic import BaseModel


class GeneralDTO(BaseModel):
    enterprise_id: int
    truck_id: int

    distance: float
    time: float

    cost: float
    earnings: float
    profit: float

    balance: float