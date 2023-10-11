'''import libs'''
from fastapi import FastAPI
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from routers.test import router as TestRouter
from routers.ai_query import router as AIQueryRouter
from models.db import Base, engine


app = FastAPI()
load_dotenv()

Base.metadata.create_all(bind=engine)

app.include_router(TestRouter)
app.include_router(AIQueryRouter)
