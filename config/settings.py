import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://username:password@localhost:5432/database_name')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_SCHEMA = 'public'  # Default schema for production

class TestConfig:
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI', 'sqlite:///test.db')  # Use the same database URI for testing

