from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DBBase = declarative_base()
    DB_URL: str = "mysql+asyncmy://root:100%Vasco@localhost:3306/projeto_pallas"

    JWT_SECRET: str ='BGUREqcg002AhP6YOR8PN4obVmD0jnFraBYfCaklpcM'
    ALGORITHM: str = 'HS256'

    ACESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        case_sensitive = True


settings: Settings = Settings()
