from app.database import get_db
from app.models import Industry
from app.repositories import IndustryRepository


class IndustryService:
    def __init__(self, db=None):
        self.db = db if db is not None else next(get_db())
        self.industry_repository = IndustryRepository(self.db)

    def get_industry_by_id(self, industry_id):
        return self.industry_repository.get_industry_by_id(industry_id)

    def get_industry_by_name(self, industry_name):
        return self.industry_repository.get_industry_by_name(industry_name)

    def create_industry(self, raw_industry):
        industry = Industry(**raw_industry.dict())

        return self.industry_repository.create_industry(industry)

    def update_industry(self, industry):
        return self.industry_repository.update_industry(industry)

    def delete_industry(self, industry_id):
        return self.industry_repository.delete_industry(industry_id)

    def get_all_industries(self):
        return self.industry_repository.get_all_industries()

    def get_all_industry_coordinates(self):
        industries = self.get_all_industries()
        coords = []
        for industry in industries:
            address = industry.address
            temp_coords = [float(address.longitude), float(address.latitude)]
            coords.append(temp_coords)
        return coords
