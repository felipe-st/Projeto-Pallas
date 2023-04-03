from fastapi import APIRouter, status, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.usuarios_model import UsuariosModel
from schemas.usuarios_schemas import UsuariosSchemaBase
from core.deps import get_session
from core.auth import autenticar, criar_token_acesso
from core.security import gerar_hash_senha

router = APIRouter()


# POST / Signup
@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UsuariosSchemaBase,
             description='Cadastra um novo usuário, após verificar se o mesmo já existe.',
             summary='Cadastra novo usuário')
async def post_novo_usuario(usuario: UsuariosSchemaBase, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuariosModel).filter(UsuariosModel.nome == usuario.nome)
        result = await session.execute(query)
        novo_usuario: UsuariosSchemaBase = result.scalars().unique().one_or_none()

        if not novo_usuario:
            novo_usuario: UsuariosModel = UsuariosModel(nome=usuario.nome, senha=gerar_hash_senha(usuario.senha))
            session.add(novo_usuario)
            await session.commit()

            return novo_usuario



        else:
            raise HTTPException(detail='Usuário já existe', status_code=status.HTTP_409_CONFLICT)


# POST / Login
@router.post('/login',
             description='Realiza o login do usuário, gerando um token JSON de acesso.',
             summary='Realiza o login do usuário')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    usuario = await autenticar(nome=form_data.username, senha=form_data.password, db=db)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Dados de acesso incorretos!')

    return JSONResponse(content={"acess_token": criar_token_acesso(sub=usuario.id), "token_type": "bearer"}, status_code=status.HTTP_200_OK)
