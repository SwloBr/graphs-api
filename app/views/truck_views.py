from fastapi import APIRouter

from app.dto.truckDTO import CreateTruckDTO

router = APIRouter()


@router.get("/truck/all")
def get_all_trucks():
    from app.services import TruckService
    truck_service = TruckService()
    return [truck for truck in truck_service.get_trucks()]


@router.get("/truck/{truck_id}")
def get_truck(truck_id: int):
    from app.services import TruckService
    truck_service = TruckService()
    return truck_service.get_truck_by_id(truck_id)


@router.get("/truck/name/{name}")
def get_truck_by_name(name: str):
    from app.services import TruckService
    truck_service = TruckService()
    return truck_service.get_truck_by_name(name)


@router.post("/truck")
def create_truck(raw_truck: CreateTruckDTO):
    from app.services import TruckService
    truck_service = TruckService()
    return truck_service.create_truck(raw_truck)
