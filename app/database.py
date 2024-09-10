# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings


# Database connection
# Configure the database connection on .env.example file
engine = create_engine(settings.sqlalchemy_database_url,
                       pool_size=10,  # Connection pool size
                       max_overflow=20,  # Maximum number of connections beyond pool_size
                       pool_timeout=30,  # Maximum time waiting for an available connection
                       pool_recycle=1800  # Time in seconds to recycle connections
                       )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Create a database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
