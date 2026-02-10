"""Модели SQLAlchemy."""

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime


class Base(DeclarativeBase):
    """Базовый класс моделей."""
    pass


class User(Base):
    """Пользователь бота."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, nullable=False, index=True)
    username = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)


class Analysis(Base):
    """Запись анализа объявления."""
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    listing_url = Column(String(1024), nullable=False)
    result_text = Column(String(8192), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
