from sqlalchemy import create_engine

from models import Base  # noqa: F401


def init_db(url: str) -> None:
    """Create all tables for the given database URL."""
    engine = create_engine(url)
    Base.metadata.create_all(bind=engine)
