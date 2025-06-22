from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, DateTime, func

Base = declarative_base()

class TimestampMixin:
    """Mixin with created/updated timestamps."""

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
