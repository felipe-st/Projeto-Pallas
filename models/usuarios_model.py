from sqlalchemy import Integer, String, Column
from core.configs import Settings


class Usuarios(Settings.DBBase):
    __tablename__ ='usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30), nullable=False)
    senha = Column(String(30), nullable=False)
