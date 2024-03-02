from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sett_data import *

# Подключение к БД
asengine = create_async_engine(
    url=f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    echo=True
)

# Сессия БД, делаем запросы
session = async_sessionmaker(bind=asengine)

#Declarative Base
class MainBase(AsyncAttrs, DeclarativeBase):
    pass