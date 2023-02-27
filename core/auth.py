from fastapi.security import OAuth2PasswordBearer

from pytz import timezone

from datetime import datetime, timedelta

from core.configs import settings

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from typing import Optional

from models.usuarios_model import UsuariosModel
from core.security import verificar_senha

from jose import jwt

oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/usuarios/login"
)


async def autenticar(nome: str, senha: str, db: AsyncSession) -> Optional[UsuariosModel]:
    async with db as session:
        query = select(UsuariosModel).filter(UsuariosModel.nome == nome)
        result = await session.execute(query)
        usuario: UsuariosModel = result.scalars().unique().one_or_none()

        if not usuario:
            return None

        if not verificar_senha(senha, usuario.senha):
            return None

        return usuario


def _criar_token(tipo_token: str, tempo_de_vida: timedelta, sub: str) -> str:
    payload = {}
    sp = timezone('America/Sao_Paulo')
    expira = datetime.now(tz=sp) + tempo_de_vida

    payload["type"] = tipo_token

    payload["exp"] = expira

    payload["iat"] = datetime.now(tz=sp)

    payload["sub"] = str(sub)

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)


def criar_token_acesso(sub: str) -> str:
    return _criar_token(
        tipo_token='acess_token',
        tempo_de_vida=timedelta(minutes=settings.ACESS_TOKEN_EXPIRE_MINUTES),
        sub=sub
    )
