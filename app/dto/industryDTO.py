from pydantic import BaseModel


class CreateIndustryDTO(BaseModel):
    name: str
    address_id: int
    price: float

    class Config:
        from_attributes = True


class IndustryDTO(BaseModel):
    id: int
    name: str
    address_id: int
    price: float

    class Config:
        from_attributes = True
