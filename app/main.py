from fastapi import FastAPI
from .authentication import auth_router


app = FastAPI()


@app.get('/')
async def home():
    return 'Home'


app.include_router(auth_router)
