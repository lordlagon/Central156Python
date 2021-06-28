
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
class CountAno:
  def __init__(self, ano, count):
    self.ano = ano
    self.count = count

anos = {2014,2015,2016,2017,2018,2019,2020,2021}
CONSULTA =[]
query = "SELECT T.FK_tipo, Mes, Ano FROM olap_156.fato_central156 C inner join dim_tipo T inner join dim_Data D where C.FK_Tipo = T.FK_Tipo and C.FK_Data = D.FK_Data and T.FK_Tipo = 5"
df = pd.read_sql(query, mydb)
CONSULTA.append(df)
print(df)

print(CONSULTA)

ANOS = []

for ano in anos:
  rdf = df.loc[(df['Mes']=='Jan') & (df['FK_tipo'] == 5) & (df['Ano']==ano)]
  result = rdf.to_json(orient="records")
  print(result)
  parsed = json.loads(result)
  count = len(parsed)
  print(count)