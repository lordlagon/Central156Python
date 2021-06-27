import mysql.connector
from numpy import number
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

api = Namespace('analises', description='Api das analises da central 156')

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

        QUANTIDADES.sort(key=get_ano)
        return QUANTIDADES

def get_ano(consulta):
    return consulta.get('ano')


countAno = api.model('countano', {
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
        COUNTANOS.clear
        query = "SELECT T.FK_tipo, mes, ano FROM olap_156.fato_central156 C inner join dim_tipo T inner join dim_Data D where C.FK_Tipo = T.FK_Tipo and C.FK_Data = D.FK_Data and T.FK_Tipo = {}".format(tipo)
        df = pd.read_sql(query, mydb)
        for ano in anos:
            rdf = df.loc[(df['mes']=='Jan') & (df['FK_tipo'] == 5) & (df['ano']==ano)]
            result = rdf.to_json(orient="records")
            #print(result)
            parsed = json.loads(result)
            count = len(parsed)
            print(count)
            countAno = {'ano': ano, 'count': count}
            print(countAno)
            COUNTANOS.append(countAno)
        COUNTANOS.sort(key=get_ano)
        return COUNTANOS
        

