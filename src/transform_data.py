import pandas as pd

def clean_data(df):
    # Ajustar os valores da coluna 'Market Share (%)' para duas casas decimais
    df['Market Share (%)'] = df['Market Share (%)'].round(2)


    return df
