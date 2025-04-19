from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Recommendation System"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Database settings
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "new.pass3"
    POSTGRES_DB: str = "recommendation_db"
    POSTGRES_PORT: str = "5432"
    
    # JWT settings
    SECRET_KEY: str = "your-secret-key-here"  # Change this in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        case_sensitive = True

settings = Settings()

# Database URL
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}" 