from sqlalchemy import create_engine,URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
url_object = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("DB_USER","fastapi_user"),
    password=os.getenv("DB_PASSWORD","fastapi1234"),
    host=os.getenv("DB_HOST","localhost"),
    port=os.getenv("DB_PORT","6543"),
    database=os.getenv("DB_NAME","fastapi_db")
)
engine=create_engine(url_object, pool_size=20,echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()