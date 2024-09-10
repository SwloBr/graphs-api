from fastapi import APIRouter

from app.dto.addressDTO import AddressDTO, CreateAddressDTO

router = APIRouter()


@router.get("/address/all")
def get_all_addresses():
    from app.services import AddressService
    address_service = AddressService()
    return [AddressDTO.model_validate(address) for address in address_service.get_all_addresses()]


@router.get("/address/{address_id}")
def get_address(address_id: int):
    from app.services import AddressService
    address_service = AddressService()
    return AddressDTO.model_validate(address_service.get_address(address_id))


@router.post("/address")
def create_address(raw_address: CreateAddressDTO):
    from app.services import AddressService
    address_service = AddressService()

    address = address_service.create_address(raw_address)
    return AddressDTO.model_validate(address)
