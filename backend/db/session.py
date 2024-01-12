from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

#create an engine for our postgresql
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#creating sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)