from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.deps import get_current_user, get_session
from models.usuarios_model import UsuariosModel
from models.lista_model import ListaModel
from schemas.lista_schemas import ListaSchemaBase

router = APIRouter()


#POST lista
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ListaSchemaBase)
async def post_lista(lista: ListaSchemaBase, usuario_logado: UsuariosModel = Depends(get_current_user), db: AsyncSession=Depends(get_session)):
    novo_item_lista: ListaModel = ListaModel(produto=lista.produto, quantidade=lista.quantidade, preco=lista.preco, usuario_id=usuario_logado.id)
    print(f'Usuario logado: {usuario_logado.id}')
    novo_item_lista.preco = novo_item_lista.quantidade*novo_item_lista.preco

    db.add(novo_item_lista)
    await db.commit()

    return novo_item_lista


#GET lista
@router.get('/', response_model=List[ListaSchemaBase])
async def get_lista(usuario_logado: UsuariosModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ListaModel).filter(ListaModel.usuario_id == usuario_logado.id)
        result = await session.execute(query)
        lista_completa: List[ListaModel] = result.scalars().unique().all()

        return lista_completa


#PUT lista
@router.put('/{linha_lista_id}', response_model=ListaSchemaBase, status_code=status.HTTP_202_ACCEPTED)
async def put_lista(linha_lista_id: int, lista: ListaSchemaBase, db: AsyncSession = Depends(get_session), usuario_logado: UsuariosModel = Depends(get_current_user)):
    async with db as session:
        query = select(ListaModel).filter(ListaModel.id == linha_lista_id).filter(ListaModel.usuario_id == usuario_logado.id)
        result = await session.execute(query)
        lista_up: ListaModel = result.scalars().unique().one_or_none()

        if lista_up:
            if lista_up.produto:
                lista_up.produto = lista.produto
            if lista_up.quantidade:
                lista_up.quantidade = lista.quantidade
            if lista_up.preco:
                lista_up.preco = lista.preco

            await session.commit()

            return lista_up
        else:
            raise HTTPException(detail='Item da lista não encontrada', status_code=status.HTTP_404_NOT_FOUND)


#DELETE item lista:
@router.delete('/{linha_lista_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_item_lista(linha_lista_id: int, db:AsyncSession = Depends(get_session), usuario_logado: UsuariosModel = Depends(get_current_user)):
    async with db as session:
        query = select(ListaModel).filter(ListaModel.id == linha_lista_id).filter(ListaModel.usuario_id == usuario_logado.id)
        result = await session.execute(query)
        item_del: ListaModel = result.scalars().unique().one_or_none()

        if item_del:
            await session.delete(item_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='item não encontrado', status_code=status.HTTP_404_NOT_FOUND)

