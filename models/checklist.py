from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin

class Checklist(Base, TimestampMixin):
    """Track completion of required documents."""

    __tablename__ = "checklists"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    items = Column(JSON, nullable=False)
    is_complete = Column(Boolean, nullable=False, server_default='0')

    user = relationship("User", back_populates="checklists")
