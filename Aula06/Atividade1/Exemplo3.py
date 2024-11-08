import os

os.system('cls')


from sqlalchemy import create_engine
import pandas as pd


host = 'localhost'
user = 'root'
password = 'root'
database = 'bd_vendas'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

query_clientes = 'SELECT id_cliente, nome, email FROM tb_clientes'
df_clientes = pd.read_sql(query_clientes, engine)
# print(df_clientes)

df_pedidos = pd.read_excel('tb_pedidos.xlsx')
# print(df_pedidos)

df_relacionado = pd.merge(df_pedidos, df_clientes, on='id_cliente', how='inner')
df_relacionado = df_relacionado.sort_values(by='nome')
print(df_relacionado)