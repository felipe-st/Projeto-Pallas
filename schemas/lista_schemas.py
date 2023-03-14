from typing import Optional

from pydantic import BaseModel


class ListaSchemaBase(BaseModel):
    id: Optional[int] = None
    produto: str
    quantidade: Optional[int] = None
    preco: float
    usuario_id: int
