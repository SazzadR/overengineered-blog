from sqlalchemy import create_engine, NullPool
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from src.config import settings

engine = create_engine(str(settings.DATABASE_URL), poolclass=NullPool)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
