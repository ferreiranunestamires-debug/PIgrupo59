import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Dashboard de Acidentes SP", layout="wide")

st.title("Análise de Acidentes de Trânsito - Estado de SP")
st.write("Projeto Integrador - Grupo 59")

# Carregar os dados
@st.cache_data
def load_data():
    # Lendo o arquivo e filtrando apenas SP na hora
    df = pd.read_csv('data/base_tratada.csv', sep=';', encoding='latin-1')
    # Garantindo que só apareça SP
    df_sp = df[df['uf'] == 'SP']
    return df_sp

try:
    df = load_data()

    # Mostrar o número total de acidentes apenas em SP
    st.metric("Total de Acidentes em São Paulo", len(df))

    # Criar o gráfico das 10 cidades com mais acidentes em SP
    st.subheader("Top 10 Municípios com mais acidentes (Apenas SP)")
    top_cidades = df['municipio'].value_counts().head(10)
    st.bar_chart(top_cidades)

except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")
