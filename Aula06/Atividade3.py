import os

os.system('cls')

import pandas as pd
import numpy as np


try:
    print('Obtendo dados...')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    df_estelionato = df_ocorrencias[['estelionato', 'mes_ano']]
    df_estelionato = df_estelionato.groupby(['mes_ano']).sum(['estelionato']).reset_index()
    print(df_estelionato.head())
    print('\nDados obtidos com sucesso!')

except Exception as e:
  print(f'Erro ao obter dados: {e}')
  exit()

try:
    df_estelionato_mes_ano = df_estelionato.groupby(['mes_ano']).sum().reset_index()
    print(df_estelionato_mes_ano)
    array_estelionato_mes_ano = np.array(df_estelionato['estelionato'])
    print('\nCalculando informações sobre padrão de estelionatos...')
    media_estelionato = (np.mean(array_estelionato_mes_ano))
    mediana_estelionato = (np.median(array_estelionato_mes_ano))
    distancia = abs(media_estelionato - mediana_estelionato) / mediana_estelionato * 100
   
   print(f'A média dos estelionatos registrados são de {media_estelionato:.2f}')
   print(f'A mediana dos estelionatos registrados são de {mediana_estelionato:.2f}')
   print(f'Índice de verificação de tendência central: {distancia:.2f}%')
   print('Baseando-se nos dados apresentados, é correto afirmar que há uma assimetria considerável, tendo em vista o padrão instável de ocorrências de estelionato ao longo do tempo')
except Exception as e:
   print(f'Erro ao obter informações sobre padrão de estelionatos: {e}')
   exit()
