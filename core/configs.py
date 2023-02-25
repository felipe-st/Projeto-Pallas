from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DBBase = declarative_base()
    DB_URL: str = "mysql+asyncmy://root:100%Vasco@localhost:3306/projeto_pallas"

    class Config:
        case_sensitive = True


settings: Settings = Settings()
