from sqlite3 import connect
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_UR = "postgresql://postgres:azerty@localhost:5432/featyou"

engine = create_engine(
    SQLALCHEMY_DATABASE_UR, connect_args = {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()