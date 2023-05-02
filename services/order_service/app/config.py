from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    LOG_LEVEL: str
    PORT: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()