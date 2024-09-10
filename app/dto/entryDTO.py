from pydantic import BaseModel


class EntryCoordDTO(BaseModel):
    tons: int
    longitude: float
    latitude: float

class EntryStringDTO(BaseModel):
    tons: int
    address: str