import re
from pydantic import (
    BaseModel, EmailStr, Field,
    field_validator
)
from datetime import (
    date as d,
    time as t,
    datetime as dt,
)
from app.core import (
    IncorrectFormatException,
)


class LoginModel(BaseModel):
    email: EmailStr = Field(
        ...,
        description='Электронная почта пользователя'
    )
    password: str = Field(
        ...,
        min_length=8,
        description='Пароль пользователя'
    )

    @field_validator('email')
    @classmethod
    def validate_phone_number(cls, values: str) -> str:
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', values):
            raise IncorrectFormatException
        return values


class RegistrationModel(LoginModel):
    first_name: str = Field(
        ...,
        description='Имя пользователя'
    )
    last_name: str = Field(
        ...,
        description='Фамилия пользователя'
    )
    patronymic: str = Field(
        ...,
        description='Отчество пользователя'
    )
    date_of_birth: d = Field(
        ...,
        description='Дата рождения пользователя'
    )
    time_of_birth: t = Field(
        ...,
        description='Время рождения пользователя'
    )
    addres_of_birth: str = Field(
        ...,
        description='Место рождения(Город)'
    )
    phone_number: str = Field(
        ...,
        description='Номер телефона пользователя'
    )
    rep_password: str = Field(
        ...,
        min_length=8,
        description='Повтор пароля пользователя'
    )

    @field_validator('phone_number')
    @classmethod
    def validate_phone_number(cls, values: str) -> str:
        if not re.match(r'^\+\d{1,15}$', values):
            raise IncorrectFormatException
        return values

    @field_validator("date_of_birth")
    @classmethod
    def validate_date_of_birth(cls, values: d):
        if values and values >= dt.now().date():
            raise IncorrectFormatException
        return values
