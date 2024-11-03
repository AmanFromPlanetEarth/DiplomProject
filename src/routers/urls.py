from fastapi.templating import Jinja2Templates
from fastapi import Request, APIRouter


template_router = APIRouter(tags=['Главная страница'])
templates = Jinja2Templates(directory='templates')

@template_router.get('/')
def get_main_page(request: Request):
    return templates.TemplateResponse(request=request, name='home.html')