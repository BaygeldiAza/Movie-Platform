from pydantic_settings  import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str
    API_PREFIX: str

    # MySQL
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_SERVER: str
    MYSQL_PORT: str
    MYSQL_DB: str

    # JWT
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # CORS
    CORS_ORIGINS: List[str] = []

    @property
    def DATABASE_URL(self):
        return f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_SERVER}:{self.MYSQL_PORT}/{self.MYSQL_DB}"

    class Config:
        env_file = ".env"

settings = Settings()

