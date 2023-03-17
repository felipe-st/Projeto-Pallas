from typing import Optional

from pydantic import BaseModel


class ListaSchemaBase(BaseModel):
    id: Optional[int] = None
    produto: str
    quantidade: int
    preco: float
    usuario_id: Optional[int] = None

    class Config:
        orm_mode = True
