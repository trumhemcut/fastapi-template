from pydantic import  BaseSettings

class Settings(BaseSettings):
  db_server: str = "localhost"
  db_user: str = "postgres"
  db_password: str = "postgres"
  db_name: str = "postgres"
  db_port: str = "5432"

settings = Settings()