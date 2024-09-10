from fastapi import APIRouter

from app.dto.fuelDTO import FuelDTO, CreateFuelDTO

router = APIRouter()

@router.get("/fuel/all")
def get_all_fuels():
    from app.services import FuelService
    fuel_service = FuelService()
    return [FuelDTO.model_validate(fuel) for fuel in fuel_service.get_all_fuels()]

@router.get("/fuel/{fuel_id}")
def get_fuel(fuel_id: int):
    from app.services import FuelService
    fuel_service = FuelService()
    fuel = fuel_service.get_fuel_by_id(fuel_id)
    return FuelDTO.model_validate(fuel)



@router.post("/fuel")
def create_fuel(raw_fuel: CreateFuelDTO):
    from app.services import FuelService
    fuel_service = FuelService()
    return fuel_service.create_fuel(raw_fuel)