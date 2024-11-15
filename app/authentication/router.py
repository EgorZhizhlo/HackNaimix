from fastapi import APIRouter, Response, Form
from .schemas import RegistrationModel, LoginModel


auth_router = APIRouter(prefix='/auth', tags=['Авторизация'])


@auth_router.post('/reg', tags=['Регистрация'])
async def auth_registration(
        response: Response,
        user: RegistrationModel = Form(...)
        ):
    return user.dict()


@auth_router.post('/log', tags=['Вход'])
async def auth_login(
        response: Response,
        user: LoginModel = Form(...)
        ):
    return user.dict()