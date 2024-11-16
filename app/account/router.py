from fastapi import APIRouter, Response, Form, Request
from .schemas import (
    CreateWorker
)
from .dao import WorkerDAO, ZodiacStatisticDAO
from app.authentication import (
    verify_access_token
)
from app.core import (
    ForbiddenException
)


account_router = APIRouter(prefix='/account', tags=['Аккаунт'])

@account_router.get('/')
async def home(
    request: Request
        ):
    token = request.cookies.get("access_token", None)
    if token is None:
        raise ForbiddenException

    payload = await verify_access_token(token)

    return {
        'message': 'Home',
        'first_name': payload['first_name'],
        'last_name': payload['last_name'],
        'company': payload['company'],
        'email': payload['email']
    }


@account_router.post('/create_user')
async def get_people(
    request: Request,
    worker: CreateWorker = Form(...),
        ):
    token = request.cookies.get("access_token", None)
    if token is None:
        raise ForbiddenException

    payload = await verify_access_token(token)

    return worker
