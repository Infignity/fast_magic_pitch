'''import dependencies'''
from sqlalchemy import Column, Integer, String
from .db import Base


class Company(Base):
    '''company data database'''
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(String)
    title = Column(String)
