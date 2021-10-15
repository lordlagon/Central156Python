from flask_restx import Api
from .api_selecao import api as selecao_api
from .api_analises import api as analises_api

api = Api(
    version='1.0', 
    title='Central156 API',
    description='Api para o TCC Statistics 156',
    doc='/Docs'
)

api.add_namespace(analises_api)
api.add_namespace(selecao_api)
