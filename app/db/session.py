"""Сессия БД (SQLAlchemy)."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.config import DATABASE_URL
from app.db.models import Base

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session() -> Session:
    """Сессия для зависимостей."""
    return SessionLocal()


def init_db() -> None:
    """Создать таблицы."""
    Base.metadata.create_all(bind=engine)
