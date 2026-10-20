from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.config import settings

engine = create_async_engine(str(settings.DATABASE_URL))
SessionLocal = async_sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    metadata = MetaData(
        naming_convention={
            "pk": "%(table_name)s_pkey",
        }
    )


async def get_db():
    async with SessionLocal() as db:
        yield db
