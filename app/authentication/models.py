from sqlalchemy.orm import Mapped
from app.core import (
    Base, TEXT_NOT_NULL,
    TEXT_NOT_NULL_UNIQUE
)


class User(Base):
    __tablename__ = "user"

    first_name: Mapped[TEXT_NOT_NULL]
    last_name: Mapped[TEXT_NOT_NULL]
    patronymic: Mapped[TEXT_NOT_NULL]
    email: Mapped[TEXT_NOT_NULL_UNIQUE]
    password: Mapped[TEXT_NOT_NULL]
