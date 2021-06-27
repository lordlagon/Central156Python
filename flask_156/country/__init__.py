from flask_restx import Api
from .api_country import api as country_api
from .api_selecao import api as selecao_api
from .api_analises import api as analises_api

api = Api(
    version='1.0', 
    title='Central156 API',
    description='Api para o TCC Statistics 156',
)

api.add_namespace(analises_api)
api.add_namespace(selecao_api)
api.add_namespace(country_api)