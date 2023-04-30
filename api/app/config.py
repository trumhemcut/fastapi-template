from pydantic import BaseSettings

class Settings(BaseSettings):
    TENANT_ID: str
    CLIENT_ID: str
    DATABASE_URL: str
    class Config:
        env_file = ".env"

settings = Settings()
