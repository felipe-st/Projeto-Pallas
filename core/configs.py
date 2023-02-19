from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings():
    DBBase = declarative_base()
    DB_URL: str = 'mysql+asyncmy://root:100%Vasco@localhost:3306/projeto_pallas'
