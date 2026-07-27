from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# TEMP: disable database for MVP deployment

engine = None

SessionLocal = None

Base = declarative_base()


def get_db():
    return None