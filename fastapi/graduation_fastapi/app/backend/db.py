from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.dialects import registry

registry.register('snowflake', 'snowflake.sqlalchemy', 'dialect')
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/db_name"
SQLALCHEMY_DATABASE_URL = "sqlite:///test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass
