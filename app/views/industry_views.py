from fastapi import APIRouter

from app.dto.industryDTO import IndustryDTO, CreateIndustryDTO

router = APIRouter()


@router.get("/industry/all")
def get_all_industries():
    from app.services import IndustryService
    industry_service = IndustryService()
    return [IndustryDTO.model_validate(industry) for industry in industry_service.get_all_industries()]


@router.get("/industry/{industry_id}")
def get_industry(industry_id: int):
    from app.services import IndustryService
    industry_service = IndustryService()
    industry = industry_service.get_industry_by_id(industry_id)
    return IndustryDTO.model_validate(industry)


@router.get("/industry/name/{name}")
def get_industry_by_name(name: str):
    from app.services import IndustryService
    industry_service = IndustryService()
    industry = industry_service.get_industry_by_name(name)
    return IndustryDTO.model_validate(industry)


@router.post("/industry")
def create_industry(raw_industry: CreateIndustryDTO):
    from app.services import IndustryService
    industry_service = IndustryService()
    return industry_service.create_industry(raw_industry)
