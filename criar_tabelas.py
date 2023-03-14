from core.connection import engine
from core.configs import settings
from models import __all_models

async def create_tables() -> None:
    print('Criando tabelas...')

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBase.metadata.drop_all)
        await conn.run_sync(settings.DBBase.metadata.create_all)

    print('Tabelas criadas com sucesso...')


if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())
