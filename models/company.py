'''import dependencies'''
from sqlalchemy import Column, Integer, String
from .db import Base


class Company(Base):
    '''company data database'''
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, index=True)
    service_product = Column(String)
    company_data = Column(String)
    pricing = Column(String)
    solutions = Column(String)
    ai_report = Column(String)
