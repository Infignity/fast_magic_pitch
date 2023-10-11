'''lib import'''
from fastapi import APIRouter, Request, Depends, Form
from starlette.templating import Jinja2Templates
from sqlalchemy.orm import Session
from models.database import connect_db
from models.company import Company
from promptai.langopen import LangChainAI

router = APIRouter()
jin_template = Jinja2Templates(directory="templates")


@router.get("/ai_query")
def query_ai_get(
    request: Request,
    db: Session = Depends(connect_db)
):
    '''get all AI queries'''
    companies_data = db.query(Company).all()
    context = {"request": request, "data": companies_data}
    return jin_template.TemplateResponse("index.html", context)


@router.post("/ai_query")
def query_ai_post(
    request: Request,
    templates: str = Form(...),
    variables: str = Form(...),
    db: Session = Depends(connect_db),
):
    """query maker"""
    langai = LangChainAI()
    feed_back = langai.content_generator(template=templates, variable=variables)
    context = {"request": request, "data": feed_back}
    return jin_template.TemplateResponse("index.html", context)
