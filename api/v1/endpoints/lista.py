from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_current_user, get_session
from models.usuarios_model import UsuariosModel
from models.lista_model import ListaModel
from schemas.lista_schemas import ListaSchemaBase

router = APIRouter()


#POST lista
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ListaSchemaBase)
async def post_lista(lista: ListaSchemaBase, usuario_logado: UsuariosModel = Depends(get_current_user), db: AsyncSession=Depends(get_session)):
    novo_item_lista: ListaModel = ListaModel(produto=lista.produto, quantidade=lista.quantidade, preco=lista.preco, usuario_id=usuario_logado.id)

    novo_item_lista.preco = novo_item_lista.quantidade*novo_item_lista.preco

    db.add(novo_item_lista)
    await db.commit()

    return novo_item_lista