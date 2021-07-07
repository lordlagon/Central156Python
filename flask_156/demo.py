
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

# query = "SELECT * FROM fato_central156"
# df = pd.read_sql(query, mydb)

# sex_age = df[["qtd","FK_Genero", "FK_Faixa_Etaria_ibge"]]

# print(sex_age)

# correlacao = df.corr[["FK_Tipo", "FK_Faixa_Etaria_ibge"]]
# print(correlacao)


# anos = {'2014','2015','2016','2017','2018','2019','2020','2021'}
# CONSULTA =[]
# for ano in anos:
#   query = "SELECT Tipo, ano, mes, count(qtd) FROM olap_156.fato_central156 C inner join dim_tipo T inner join dim_Data D where C.FK_Tipo = T.FK_Tipo and C.FK_Data = D.FK_Data and T.FK_Tipo = 5 and D.Mes = 'jan' and D.Ano ={}".format(ano)
#   df = pd.read_sql(query, mydb)
#   CONSULTA.append(df)
#   # print(df)
# print(CONSULTA)
# class CountAno:
#   def __init__(self, ano, count):
#     self.ano = ano
#     self.count = count

# anos = {2014,2015,2016,2017,2018,2019,2020,2021}
# CONSULTA =[]
# query = "SELECT T.FK_tipo, Mes, Ano FROM olap_156.fato_central156 C inner join dim_tipo T inner join dim_Data D where C.FK_Tipo = T.FK_Tipo and C.FK_Data = D.FK_Data and T.FK_Tipo = 5"
# df = pd.read_sql(query, mydb)
# CONSULTA.append(df)
# print(df)

# print(CONSULTA)

# ANOS = []

# for ano in anos:
#   rdf = df.loc[(df['Mes']=='Jan') & (df['FK_tipo'] == 5) & (df['Ano']==ano)]
#   result = rdf.to_json(orient="records")
#   print(result)
#   parsed = json.loads(result)
#   count = len(parsed)
#   print(count)

# SOLICITACOESMES = []
# query = "SELECT assunto, subdivisao, mes, ano FROM olap_156.fato_central156 C inner join dim_assunto A inner join dim_subdivisao2 S inner join dim_Data D where S.Fk_subdivisao= C.fk_subdivisao and C.FK_Assunto = A.FK_Assunto and C.FK_Data = D.FK_Data limit 10000"
# df = pd.read_sql(query, mydb)
# # for ano in anos:
# #     for mes in meses:

# # print(df)
# # mes ='Jul'
# # ano = 2015

# # class Helpers2:
# #     def get_qntd(consulta):
# #         return consulta.get('count')

# gdf = df.groupby(['assunto','subdivisao','ano']).size().reset_index(name='count')
# mdf = gdf.sort_values(by='count', ascending=False).head(10)
# print(mdf)

query = "SELECT assunto, genero, faixa_etaria, ano FROM olap_156.fato_central156 C inner join dim_assunto A inner join dim_genero G inner join dim_Data D inner join dim_faixa_etaria_ibge F where F.FK_Faixa_Etaria_ibge = C.FK_Faixa_Etaria_ibge and C.Fk_genero = G.fk_genero and C.FK_Assunto = A.FK_Assunto and C.FK_Data = D.FK_Data and F.FK_Faixa_Etaria_ibge != 20  limit 10000"
df = pd.read_sql(query, mydb)


gdf = df.groupby(['assunto','genero','faixa_etaria']).size().reset_index(name='count')
mdf = gdf.sort_values(by='count', ascending=False)
print(mdf)

# Tipo
# Assunto
# Subdivisao
# Genero
# Mes
# Ano
#296855

