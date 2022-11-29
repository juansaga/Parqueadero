# Por medio de este script se le permite al proyecto acceder a la base de datos, 
# que en  este caso posee el nombre de "sql_app.db"

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Session:
    """ Método para obtener la base de datos"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()