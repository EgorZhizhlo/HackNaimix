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


class CreateWorker(BaseModel):
    first_name: str = Field(
        ...,
        description='Имя сотрудника'
    )
    last_name: str = Field(
        ...,
        description='Фамилия сотрудника'
    )
    patronymic: str = Field(
        ...,
        description='Отчество сотрудника'
    )
    position: str = Field(
        ...,
        description='Должность сотрудника'
    )
    date_of_birth: d = Field(
        ...,
        description='Дата рождения сотрудника'
    )
    time_of_birth: t = Field(
        ...,
        default_factory=lambda: t(12, 0),
        description='Время рождения сотрудника'
    )
    addres_of_birth: str = Field(
        ...,
        description='Место рождения сотрудника'
    )

    @field_validator("date_of_birth")
    @classmethod
    def validate_date_of_birth(cls, values: d):
        if values and values >= dt.now().date():
            raise IncorrectFormatException
        return values
