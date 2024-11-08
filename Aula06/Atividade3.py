import os

os.system('cls')

import pandas as pd
import numpy as np


try:
    print('Obtendo dados...')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    df_estelionato = df_ocorrencias[['mes', 'estelionato']]
    df_estelionato = df_estelionato.groupby(['mes']).sum(['estelionato']).reset_index()
    print(df_estelionato.head())
    print('\nDados obtidos com sucesso!')

except Exception as e:
  print(f'Erro ao obter dados: {e}')
  exit()

try:
   print('\nCalculando informações sobre padrão de estelionatos...')
   array_estelionato = np.array(df_estelionato['estelionato'])
   media_estelionato = int(np.mean(array_estelionato))
   mediana_estelionato = int(np.median(array_estelionato))
   distancia = abs(media_estelionato - mediana_estelionato) / mediana_estelionato * 100
   
   print(f'A média dos estelionatos registrados são de {media_estelionato}')
   print(f'A mediana dos estelionatos registrados são de {mediana_estelionato}')
   print(f'Índice de verificação de tendência central: {distancia:.2f}%')
   print('Baseando-se nos dados apresentados, é correto afirmar que há um padrão estável de ocorrências de estelionato ao longo do tempo')
except Exception as e:
   print(f'Erro ao obter informações sobre padrão de estelionatos: {e}')
   exit()