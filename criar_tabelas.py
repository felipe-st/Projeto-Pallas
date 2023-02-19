from core.connection import engine
from core.configs import Settings

async def create_tables() -> None:
    print('Criando tabelas...')

    async with engine.begin() as conn:
        await conn.run_sync(Settings.DBBase.metadata.drop_all)
        await conn.run_sync(Settings.DBBase.metadata.create_all)

    print('Tabelas criadas com sucesso...')


if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())
