from sqlalchemy import Numeric, Integer, String, ForeignKey, Column
from sqlalchemy.orm import relationship

from core.configs import settings


class ListaModel(settings.DBBase):
    __tablename__ = 'lista'

    id = Column(Integer, primary_key=True)
    produto = Column(String(50), nullable=False)
    quantidade = Column(Integer, nullable=True)
    preco = Column(Numeric(3), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    usuarios = relationship("UsuariosModel", backref="usuarios", lazy="subquery")
