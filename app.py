'''import libs'''
from fastapi import FastAPI
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from routers.test import router as TestRouter
from routers.ai_query import router as AIQueryRouter


app = FastAPI()
load_dotenv()

app.include_router(TestRouter)
app.include_router(AIQueryRouter)