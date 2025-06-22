from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin

class Document(Base, TimestampMixin):
    """User uploaded document."""

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    filename = Column(String, nullable=False)
    content_type = Column(String, nullable=False)
    url = Column(String, nullable=False)

    user = relationship("User", back_populates="documents")
