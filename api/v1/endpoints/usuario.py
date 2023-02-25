from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.usuarios_model import UsuariosModel
from schemas.usuarios_schemas import UsuariosSchemaBase
from core.deps import get_session


router = APIRouter()


# POST / Signup
@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UsuariosSchemaBase)
async def post_novo_usuario(usuario: UsuariosSchemaBase, db: AsyncSession = Depends(get_session)):
#    novo_usuario: UsuariosModel = UsuariosModel(nome=usuario.nome, senha=usuario.senha)
    async with db as session:
        query = select(UsuariosModel).filter(UsuariosModel.nome == usuario.nome)
        result = await session.execute(query)
        novo_usuario: UsuariosSchemaBase = result.scalars().unique().one_or_none()

        if not novo_usuario:
            novo_usuario: UsuariosModel = UsuariosModel(nome=usuario.nome, senha=usuario.senha)
            session.add(novo_usuario)
            await session.commit()

            return novo_usuario

        else:
            raise HTTPException(detail='Usuário já existe', status_code=status.HTTP_409_CONFLICT)
