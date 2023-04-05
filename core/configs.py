from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DBBase = declarative_base()
    DB_URL: str = ""

    JWT_SECRET: str =''
    ALGORITHM: str = 'HS256'

    ACESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        case_sensitive = True


settings: Settings = Settings()
