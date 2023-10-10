"""importing fast api and other dependencies"""
from fastapi import FastAPI, Request, Depends, Form
# from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from models.company import Company
from models.db import SessionLocal, engine, Base

# defining the app
app = FastAPI()

# load enviromental varibles
load_dotenv()

# pre create database if not exist
Base.metadata.create_all(bind=engine)

# setting template directory
templates = Jinja2Templates(directory="templates")


# connect to database
def connect_db():
    """database connect"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home_page():
    '''starter test page'''
    return {"Hello": "World"}


@app.get("/ai_query")
def query_ai_get(
    request: Request,
    db: Session = Depends(connect_db)
    ): 
    """display template for queries"""
    companies_data = db.query(Company).all()
    context = {
        "request": request,
        "data": companies_data
        }
    return templates.TemplateResponse(
        "index.html",
        context
    )


@app.post("/ai_query")
def query_ai_post(
    request: Request,
    title: str = Form(...),
    db: Session = Depends(connect_db)
    ):
    """query langchain"""
    company = Company()
    db.add(new_todo)
    db.commit()
    pass

