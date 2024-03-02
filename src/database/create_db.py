from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, as_declarative, declared_attr
from src.sett_data import *

# Подключение к БД
as_engine = create_async_engine(
    url=f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    echo=True
)

# Сессия БД, делаем запросы
session = async_sessionmaker(bind=as_engine)


# Declarative Base
@as_declarative()
class MainBase(AsyncAttrs, DeclarativeBase):

    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


async def create_database():
    #Создаем все таблицы из MetaData

    async with as_engine.begin() as conn:
        await conn.run_sync(
            MainBase.metadata.create_all
        )