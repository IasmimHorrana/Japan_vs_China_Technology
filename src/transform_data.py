import pandas as pd

# Formata o valor como uma string em formato de moeda USD com separadores de milhares.
def format_usd(value):
    return f"${value:,.2f}"

# Ajustar os valores da coluna 'Market Share (%)' para duas casas decimais
def clean_data(df):
    df['Market Share (%)'] = df['Market Share (%)'].round(2)
    df['Internet Penetration (%)'] = df['Internet Penetration (%)'].round(2)
    df['5G Network Coverage (%)'] = df['5G Network Coverage (%)'].round(2)
    
    # Formata o valor
    df['R&D Investment (in USD)'] = df['R&D Investment (in USD)'].apply(lambda x: f"${x:,.2f}")
    df['Venture Capital Funding (in USD)'] = df['Venture Capital Funding (in USD)'].apply(lambda x: f"${x:,.2f}")
    df['Tech Exports (in USD)'] = df['Tech Exports (in USD)'].apply(lambda x: f"${x:,.2f}")

    return df
