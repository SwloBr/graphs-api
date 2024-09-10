from sqlalchemy.orm import Session

from app.models import Industry


class IndustryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_industry_by_id(self, industry_id: int):
        return self.db.query(Industry).filter(industry_id == Industry.id).first()

    def get_industry_by_name(self, industry_name: str):
        return self.db.query(Industry).filter(industry_name == Industry.name).first()

    def create_industry(self, industry: Industry):
        self.db.add(industry)
        self.db.commit()
        self.db.refresh(industry)
        return industry

    def update_industry(self, industry: Industry, **fields):
        for key, value in fields.items():
            setattr(industry, key, value)
        self.db.commit()
        self.db.refresh(industry)
        return industry

    def delete_industry(self, industry: Industry):
        self.db.delete(industry)
        self.db.commit()
        return industry

    def get_all_industries(self):
        return self.db.query(Industry).all()