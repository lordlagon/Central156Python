from flask_restx import Namespace, Resource, fields

import mysql.connector
import pandas as pd
import json

# Conexão Mysql
mydb = mysql.connector.connect(
  host="localhost",
  port="3305",
  user="root",
  password="root",
  database="olap_156"
)

api = Namespace('analises', description='Api das analises da central 156')

class Helpers:
    def get_ano(consulta):
        return consulta.get('ano')

consulta = api.model('consulta', {
    'tipo': fields.String(required=True, description='nome do Tipo'),
    'mes': fields.String(description='Mês das solicitações'),
    'ano': fields.Integer(),
    'count': fields.Integer()
})



QUANTIDADES = []
anos = {2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021}

@api.route('/consulta/<tipo>/<mes>')
@api.param('<tipo>')
@api.param('<mes>')
@api.response(404, 'Not found')
class ConsultaList(Resource):
    @api.doc('list_consulta')
    @api.marshal_list_with(consulta)
    def get(self, tipo, mes):
        QUANTIDADES.clear
        for ano in anos:
            query = "SELECT tipo, ano, mes, count(qtd) as count FROM olap_156.fato_central156 C inner join dim_tipo T inner join dim_Data D where C.FK_Tipo = T.FK_Tipo and C.FK_Data = D.FK_Data and T.FK_Tipo = {} and D.Ano ={} and D.mes='{}'".format(tipo, ano, mes)
            df = pd.read_sql(query, mydb)
            result = df.to_json(orient="records")
            parsed = json.loads(result)
            for item in parsed:
                if item['tipo'] is not None:
                    QUANTIDADES.append(item)

        QUANTIDADES.sort(key=Helpers.get_ano)
        return QUANTIDADES




countAno = api.model('countano', {
    'tipo': fields.String(description='nome do Tipo'),
    'mes': fields.String(description='Mês das solicitações'),
    'ano': fields.Integer(),
    'count': fields.Integer()

})
COUNTANOS = []

@api.route('/countano/<tipo>/<mes>')
@api.param('<tipo>')
@api.param('<mes>')
@api.response(404, 'Not found')
class ConsultaCountAno(Resource):
    @api.doc('list_countAno')
    @api.marshal_list_with(countAno)
    def get(self, tipo, mes):
        print(tipo, mes)
        COUNTANOS.clear()
        query = "SELECT T.FK_tipo, mes, ano FROM olap_156.fato_central156 C inner join dim_tipo T inner join dim_Data D where C.FK_Tipo = T.FK_Tipo and C.FK_Data = D.FK_Data and T.FK_Tipo = {}".format(tipo)
        df = pd.read_sql(query, mydb)
        for ano in anos:
            options = [mes]
            rdf = df.loc[(df['mes'].isin(options)) & (df['ano']==ano)]
            result = rdf.to_json(orient="records")
            parsed = json.loads(result)
            count = len(parsed)
            countAno = {'ano': ano, 'count': count, 'tipo': tipo, 'mes': mes}
            print(countAno)
            COUNTANOS.append(countAno)
        COUNTANOS.sort(key=Helpers.get_ano)
        return COUNTANOS
        
varSolicitacaoMes = api.model('varsolicitacaomes', {
    'tipo': fields.String(description='nome do Tipo'),
    'mes': fields.String(description='Mês das solicitações'),
    'ano': fields.Integer(),
    'dataCompleta': fields.DateTime(),
    'count': fields.Integer()

})
SOLICITACOESMES = []
meses = { "Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez" }
@api.route('/varsolicitacaomes')

class GetVarSolicitacaoMes(Resource):
    @api.doc('list_varSolicitacaoMes')
    @api.marshal_list_with(varSolicitacaoMes)
    def get(self):
        # if (len(SOLICITACOESMES) > 0):
        #     return SOLICITACOESMES
        query = "SELECT T.fk_tipo, tipo, mes, ano, datacompleta FROM olap_156.fato_central156 C inner join dim_tipo T inner join dim_Data D where C.FK_Tipo = T.FK_Tipo and C.FK_Data = D.FK_Data"
        df = pd.read_sql(query, mydb)
        for ano in anos:
            for mes in meses:
                rdf = df.loc[(df['mes'] == mes) & (df['ano']==ano)]
                
                print(mes, ano)
                print(rdf)

        #     rdf = df.loc[(df['mes'].isin(meses)) & (df['ano']==ano)]
        #     result = rdf.to_json(orient="records")
        #     parsed = json.loads(result)
        #     count = len(parsed)
        #     varSolicitacaoMes = {'ano': ano, 'count': count, 'tipo': tipo, 'mes': mes}
        #     print(varSolicitacaoMes)
        #     SOLICITACOESMES.append(varSolicitacaoMes)
        # SOLICITACOESMES.sort(key=Helpers.get_ano)
        return SOLICITACOESMES

