from fastapi import FastAPI

from core.configs import settings
from api.v1.api_ import api_router


app = FastAPI(title='Projeto Pallas',
              version='1.0',
              description='Uma api para backend de uma aplicação simples de lista de compras, para estudo.'
              )
app.include_router(api_router, prefix=settings.API_V1_STR)
