from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


template = Jinja2Templates(directory='templates')
greeting_router = APIRouter(prefix='/greeting')


@greeting_router.get('')

def print_message(request: Request, name, message): 
    return template.TemplateResponse('index.html', {"request": request, "name": name, "message": message})
