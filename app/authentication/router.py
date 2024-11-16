from fastapi import APIRouter, Response, Form
from .schemas import (
    RegistrationModel, LoginModel, UserAuth
)
from .dao import UserDAO
from .algorithm import (
    hash_password, authenticate_user,
    create_access_token
)
from app.core import (
    UserAlreadyExistsException,
    PasswordMismatchException,
    IncorrectEmailOrPasswordException
)


auth_router = APIRouter(prefix='/auth', tags=['Авторизация'])


@auth_router.post('/registration', response_model=UserAuth)
async def auth_registration(
        response: Response,
        user: RegistrationModel = Form(...)
):

    find_user = await UserDAO.find(
        all=False,
        or_method=False,
        email=user.email,
    )

    if find_user:
        raise UserAlreadyExistsException

    if user.password != user.rep_password:
        raise PasswordMismatchException

    hashed_password = await hash_password(user.password)

    created_user = await UserDAO.add(
        first_name=user.first_name,
        last_name=user.last_name,
        company=user.company,
        date_of_birth=user.date_of_birth,
        email=user.email,
        phone_number=user.phone_number,
        password=hashed_password
    )
    access_token = await create_access_token(
        {
            'id': created_user.id,
            'company': created_user.company,
            'first_name': created_user.first_name,
            'last_name': created_user.last_name,
            'email': created_user.email,
        }
    )
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True
    )

    return {
        'message': 'Registered successfully ',
        'first_name': created_user.first_name,
        'last_name': created_user.last_name,
        'company': created_user.company,
        'email': created_user.email
    }


@auth_router.post('/login', response_model=UserAuth)
async def auth_login(
        response: Response,
        user: LoginModel = Form(...)
):
    auth_user = await authenticate_user(
        email=user.email,
        password=user.password,
    )
    if auth_user is None:
        raise IncorrectEmailOrPasswordException

    access_token = await create_access_token(
        {
            'id': auth_user.id,
            'company': auth_user.company,
            'first_name': auth_user.first_name,
            'last_name': auth_user.last_name,
            'email': auth_user.email,
        }
    )
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True
    )
    return {
        'message': 'Logged in successfully',
        'company': auth_user.company,
        'first_name': auth_user.first_name,
        'last_name': auth_user.last_name,
        'email': auth_user.email
    }


@auth_router.post("/logout/")
async def logout_user(response: Response):
    response.delete_cookie(key="access_token")
    return {'message': 'Logged out successfully'}
