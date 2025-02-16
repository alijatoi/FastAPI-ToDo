from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from models import Base

DATABASE_URL = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'test.db')}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a SessionLocal class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables if they don't exist
Base.metadata.create_all(bind=engine)
