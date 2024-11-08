import os

os.system('cls')


from sqlalchemy import create_engine 
import numpy as np
import pandas as pd 


host = 'localhost'
user = 'root'
password = 'root'
database = 'bd_loja'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

df_estoque = pd.read_sql('tb_produtos', engine)

df_estoque['TotalEstoque'] = df_estoque['QuantidadeEstoque'] * df_estoque['Valor']
df_agrupado = df_estoque.groupby('NomeProduto').agg({'QuantidadeEstoque': 'sum', 'TotalEstoque': 'sum'}).reset_index()
df_ordenado = df_agrupado.sort_values(by='TotalEstoque', ascending=False)

produto = df_estoque['NomeProduto']
precos = df_estoque['Valor']

media_precos = np.median(precos)

q1 = np.quantile(precos, 0.25)
q2 = np.quantile(precos, 0.50)
q3 = np.quantile(precos, 0.75)

print(f'O preço médio dos produtos é: R${media_precos}')
print(f'25% dos produtos em estoque têm o preço inferior a R${q1}')
print(f'50% dos produtos em estoque têm o preço inferior a R${q2}')
print(f'75% dos produtos em estoque têm o preço inferior a R${q3}')

array_total_estoque = np.array(df_estoque["TotalEstoque"])

media = np.mean(array_total_estoque)
mediana = np.median(array_total_estoque)
distancia = abs(media - mediana)/ mediana * 100

print(media)
print(mediana)
print(distancia)

print(df_agrupado)
print(df_ordenado[['NomeProduto', "TotalEstoque"]])

