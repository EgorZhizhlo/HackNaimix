from app.core import BaseDAO
from .models import Worker, ZodiacStatistic


class WorkerDAO(BaseDAO):
    model = Worker


class ZodiacStatisticDAO(BaseDAO):
    model = ZodiacStatistic
