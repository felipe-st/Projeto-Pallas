from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from core.configs import settings


class UsuariosModel(settings.DBBase):
    __tablename__ ='usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30), nullable=True)
    senha = Column(String(100), nullable=True)
