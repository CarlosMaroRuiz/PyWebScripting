CONFIG_TEMPLATE = """from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models.base import Base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
"""