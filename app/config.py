from pydantic import BaseSettings


class Settings(BaseSettings):
    db_server: str = "localhost"
    db_user: str = "postgres"
    db_password: str = "postgres"
    db_name: str = "postgres"
    db_port: str = "5432"
    tenant_id: str = "d8ac9062-da58-40c7-87f3-2ddea9fa470f"
    client_id: str = "cc2c77c6-d78e-4e0c-90ed-ec89bd7cf1b0"


settings = Settings()
