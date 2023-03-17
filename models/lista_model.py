from sqlalchemy import Numeric, Integer, String, ForeignKey, Column
from sqlalchemy.orm import relationship

from core.configs import settings


class ListaModel(settings.DBBase):
    __tablename__ = 'lista'

    id = Column(Integer, primary_key=True, autoincrement=True)
    produto = Column(String(50))
    quantidade = Column(Integer)
    preco = Column(Numeric(6, 2, asdecimal=True))
    usuario_id = Column(Integer)
#    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

#    usuarios = relationship("UsuariosModel", backref="usuarios", lazy="subquery")
