'''lib import'''
from fastapi import APIRouter, Request, Depends, Form, Body
from starlette.templating import Jinja2Templates
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models.database import connect_db
from models.company import Company
from promptai.langopen import LangChainAI



class TranslationRequest(BaseModel):
    prompt: str

router = APIRouter()
jin_template = Jinja2Templates(directory="templates")


@router.get("/ai_query")
def query_ai_get(
    request: Request,
    db: Session = Depends(connect_db)
):
    '''get all AI queries'''
    companies_data = db.query(Company).all()
    result_list = []
    # Loop through the data and create dictionaries
    for item in companies_data:
        result_dict = {
            "id": item.id,
            "prompt": item.prompt,
        }
        result_list.append(result_dict)
    context = {"request": request, "data": result_list}
    return jin_template.TemplateResponse("index.html", context)


@router.post("/ai_query")
def query_ai_post(
    request: Request,
    prompt: TranslationRequest,
    db: Session = Depends(connect_db),
):
    """query maker"""
    new_company = Company(prompt=prompt.prompt)
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return {"status": "success", "data": new_company}

    # context = {"request": request, "data": new_company}
    # return jin_template.TemplateResponse("index.html", context)
