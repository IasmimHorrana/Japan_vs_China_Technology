import pandas as pd
from sqlalchemy import create_engine

# Conexão com o banco de dados PostgreSQL no Docker
engine = create_engine('postgresql+psycopg2://postgres:Postgres2024!@localhost:15432/postgres')

# Caminho para o CSV dentro da pasta data
csv_path = '../data/Big_Japan_vs_China_Technology.csv'

# Ler o arquivo CSV
df = pd.read_csv(csv_path)

# Inserir o DataFrame no banco de dados 
df.to_sql('dataset_table', engine, if_exists='append', index=False) #if_exists='replace'

print("Dados inseridos com sucesso!")


