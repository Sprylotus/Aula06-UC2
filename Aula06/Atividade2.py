import os

os.system('cls')

import pandas as pd
import numpy as np


try:
    print('Obtendo dados...')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]
    df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()
    print(df_roubo_veiculo.head())
    print('\nDados obtidos com sucesso!')

except Exception as e:
  print(f'Erro ao obter dados: {e}')
  exit()

try:
   print('\nCalculando informações sobre padrão de roubo de veículos...')
   array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])
   media_roubo_veiculo = int(np.mean(array_roubo_veiculo))
   mediana_roubo_veiculo = int(np.median(array_roubo_veiculo))
   distancia = abs(media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo
   print(media_roubo_veiculo)
   print(mediana_roubo_veiculo)
   print(distancia)

except Exception as e:
   print(f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
   exit()