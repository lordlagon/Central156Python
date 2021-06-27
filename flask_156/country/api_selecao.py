import mysql.connector
import pandas as pd
import json
from flask_restx import Namespace, Resource, fields

# Conexão Mysql
mydb = mysql.connector.connect(
  host="localhost",
  port="3305",
  user="root",
  password="root",
  database="olap_156"
)

api = Namespace('selecao', description='Api para selecao dos campos do statistics 156')

assunto = api.model('assunto', {
    'fk_assunto': fields.String(required=True, description='fk do assunto'),
    'assunto': fields.String(required=True, description='nome do assunto')
})

bairro = api.model('bairro', {
    'fk_bairro': fields.String(required=True, description='fk do bairro'),
    'bairro': fields.String(required=True, description='nome do bairro')
})

data = api.model('data', {
    'fk_data': fields.String(required=True, description='fk da data'),
    'datacompleta': fields.String(required=True, description='datetime da data'),
    'ano': fields.String(description='ano'),
    'mes': fields.String(description='mes'),
    'diasemana': fields.String(description='dia da semana'),
    'trimestre': fields.String(description='trimestre'),
    'semestre': fields.String(description='trimestre'),
})

faixa_etaria = api.model('faixa_etaria', {
    'fk_faixa_etaria_ibge': fields.String(required=True, description='fk do faixa_etaria'),
    'faixa_etaria': fields.String(required=True, description='nome do faixa_etaria')
})

genero = api.model('genero', {
    'fk_genero': fields.String(required=True, description='fk do genero'),
    'genero': fields.String(required=True, description='nome do genero')
})

regional = api.model('regional', {
    'fk_regional': fields.String(required=True, description='fk do regional'),
    'regional': fields.String(required=True, description='nome do regional')
})

subdivisao = api.model('subdivisao', {
    'fk_subdivisao': fields.String(required=True, description='fk do subdivisao'),
    'subdivisao': fields.String(required=True, description='nome do subdivisao')
})


tipo = api.model('tipo', {
    'fk_tipo': fields.String(required=True, description='fk do Tipo'),
    'tipo': fields.String(required=True, description='nome do Tipo')
})


ASSUNTOS = []
BAIRROS = []
DATAS = []
FAIXAS_ETARIAS =[]
GENEROS = []
REGIONAIS = []
SUBDIVISOES = []
TIPOS = []

@api.route('/assuntos')
class AssuntoList(Resource):
    @api.doc('list_assuntos')
    @api.marshal_list_with(assunto)
    def get(self):
        query = "select fk_assunto, assunto from olap_156.dim_assunto where assunto is not null"
        df = pd.read_sql(query, mydb)
        result = df.to_json(orient="records")
        parsed = json.loads(result)
        for item in parsed:
            ASSUNTOS.append(item)
        return ASSUNTOS

@api.route('/bairros')
class AssuntoList(Resource):
    @api.doc('list_bairros')
    @api.marshal_list_with(bairro)
    def get(self):
        query = "select fk_bairro, bairro from olap_156.dim_bairro2 where bairro is not null;"
        df = pd.read_sql(query, mydb)
        result = df.to_json(orient="records")
        parsed = json.loads(result)
        for item in parsed:
            BAIRROS.append(item)
        return BAIRROS

@api.route('/datas')
class AssuntoList(Resource):
    @api.doc('list_data')
    @api.marshal_list_with(data)
    def get(self):
        query = "select fk_data, datacompleta, ano, diasemana, mes, trimestre, semestre from olap_156.dim_data where DataCompleta is not null"
        df = pd.read_sql(query, mydb)
        result = df.to_json(orient="records")
        parsed = json.loads(result)
        for item in parsed:
            DATAS.append(item)
        return DATAS

@api.route('/faixa_etaria')
class FaixaEtariaList(Resource):
    @api.doc('list_faixa_etaria')
    @api.marshal_list_with(faixa_etaria)
    def get(self):
        query = "select fk_faixa_etaria_ibge, faixa_etaria FROM olap_156.dim_faixa_etaria_ibge where faixa_etaria is not null;"
        df = pd.read_sql(query, mydb)
        result = df.to_json(orient="records")
        print(result)
        parsed = json.loads(result)
        for item in parsed:
            FAIXAS_ETARIAS.append(item)
        return FAIXAS_ETARIAS

@api.route('/generos')
class GeneroList(Resource):
    @api.doc('list_generos')
    @api.marshal_list_with(genero)
    def get(self):
        query = "select fk_genero, genero from olap_156.dim_genero where genero is not null"
        df = pd.read_sql(query, mydb)
        result = df.to_json(orient="records")
        print(result)
        parsed = json.loads(result)
        for item in parsed:
            GENEROS.append(item)
        return GENEROS

@api.route('/regionais')
class RegionalList(Resource):
    @api.doc('list_regionais')
    @api.marshal_list_with(regional)
    def get(self):
        query = "select fk_regional, regional from olap_156.dim_regional where regional is not null"
        df = pd.read_sql(query, mydb)
        result = df.to_json(orient="records")
        print(result)
        parsed = json.loads(result)
        for item in parsed:
            REGIONAIS.append(item)
        return REGIONAIS

@api.route('/subdivisao')
class SubdivisaoList(Resource):
    @api.doc('list_subdivisao')
    @api.marshal_list_with(subdivisao)
    def get(self):
        query = "select fk_subdivisao, subdivisao from olap_156.dim_subdivisao2 where subdivisao is not null"
        df = pd.read_sql(query, mydb)
        result = df.to_json(orient="records")
        print(result)
        parsed = json.loads(result)
        for item in parsed:
            SUBDIVISOES.append(item)
        return SUBDIVISOES

@api.route('/tipos')
class TipoList(Resource):
    @api.doc('list_types')
    @api.marshal_list_with(tipo)
    def get(self):
        query = "select fk_tipo, tipo from olap_156.dim_tipo where tipo is not null"
        df = pd.read_sql(query, mydb)
        result = df.to_json(orient="records")
        
        parsed = json.loads(result)
        for item in parsed:
            TIPOS.append(item)
        print(TIPOS)
        return TIPOS
