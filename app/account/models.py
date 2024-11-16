from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.core import (
    Base, TEXT_NOT_NULL, TEXT_NOT_NULL_UNIQUE,
    DATE_NOT_NULL, TIME_NOT_NULL
)


class Worker(Base):
    __tablename__ = "worker"

    first_name: Mapped[TEXT_NOT_NULL]
    last_name: Mapped[TEXT_NOT_NULL]
    patronymic: Mapped[TEXT_NOT_NULL]
    position: Mapped[TEXT_NOT_NULL]
    date_of_birth: Mapped[DATE_NOT_NULL]
    time_of_birth: Mapped[TIME_NOT_NULL]
    city_of_birth: Mapped[TEXT_NOT_NULL]
    zodiac_sign: Mapped[TEXT_NOT_NULL]
    house_1: Mapped[TEXT_NOT_NULL]
    house_2: Mapped[TEXT_NOT_NULL]
    house_6: Mapped[TEXT_NOT_NULL]
    house_7: Mapped[TEXT_NOT_NULL]
    house_9: Mapped[TEXT_NOT_NULL]
    house_10: Mapped[TEXT_NOT_NULL]
    house_11: Mapped[TEXT_NOT_NULL]

    extend_existing = True

# class Company(Base):
#     __tablename__ = "company"


class ZodiacStatistic(Base):
    __tablename__ = "zodiac_statistic"

    company: Mapped[TEXT_NOT_NULL]
    team: Mapped[TEXT_NOT_NULL]
    similarity_coef: Mapped[TEXT_NOT_NULL]
    worker_id: Mapped[int] = mapped_column(ForeignKey("worker.id"))

    extend_existing = True
