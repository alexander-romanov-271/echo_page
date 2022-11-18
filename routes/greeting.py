from fastapi import APIRouter

greeting_router = APIRouter(prefix='/greeting')


@greeting_router.get('')
def print_message(name, message): 
    return f'{name}! {message}'
