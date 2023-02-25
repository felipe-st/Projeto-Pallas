from typing import Optional

from pydantic import BaseModel


class UsuariosSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    senha: str

    class Config:
        orm_mode = True

