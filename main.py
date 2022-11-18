from fastapi import FastAPI
from routes import greeting_router

app = FastAPI()
app.include_router(greeting_router)
