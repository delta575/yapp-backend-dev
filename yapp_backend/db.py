import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Get DATABASE_URL from .env file
load_dotenv()
database_url = os.getenv("DATABASE_URL")

# Create engine
engine = create_engine(database_url)

# Create Session Maker
Session = sessionmaker(bind=engine)

# Create Base schema Class
Base = declarative_base()
