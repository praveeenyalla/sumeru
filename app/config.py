import os
from pydantic import BaseModel

class Settings(BaseModel):
    APP_NAME: str = os.getenv("APP_NAME", "Sumeru Technologies LLC | Enterprise Technology, Consulting & IT Solutions")
    APP_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./sumeru_enterprise.db")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    ALLOWED_ORIGINS: list[str] = [
        origin.strip()
        for origin in os.getenv("ALLOWED_ORIGINS", "*").split(",")
        if origin.strip()
    ]

settings = Settings()
