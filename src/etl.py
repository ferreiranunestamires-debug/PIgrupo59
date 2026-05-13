
import pandas as pd

# 1. Extração: Carregar os dados originais
print("Carregando a base original...")
df = pd.read_csv('../data/base_original.csv', sep=';', encoding='utf-8')

# 2. Transformação: Filtrar apenas o estado de SP
print("Filtrando dados de São Paulo...")
df_sp = df[df['uf'] == 'SP']

# Remover linhas que não tenham o nome do município preenchido
df_sp = df_sp.dropna(subset=['municipio'])

# 3. Carga: Salvar a base tratada para o dashboard usar
df_sp.to_csv('../data/base_tratada.csv', index=False, sep=';')
print("ETL concluído! A base_tratada.csv foi gerada com sucesso.")
