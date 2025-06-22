from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin

class User(Base, TimestampMixin):
    """Application user."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, server_default='1')
    role = Column(String, nullable=False, server_default='student')

    documents = relationship("Document", back_populates="user", cascade="all, delete-orphan")
    checklists = relationship("Checklist", back_populates="user", cascade="all, delete-orphan")
