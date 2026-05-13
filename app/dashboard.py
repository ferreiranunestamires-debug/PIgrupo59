
import streamlit as st
import pandas as pd

# Título da página
st.title("Análise de Acidentes de Trânsito - SP")
st.write("Projeto Integrador - Grupo 59")

# Carregar a base tratada
@st.cache_data
def load_data():
    return pd.read_csv('../data/base_tratada.csv', sep=';')

df = load_data()

# Métrica Geral
st.metric("Total de Acidentes Analisados em SP", len(df))

# Gráfico de Barras: Top 10 cidades com mais acidentes
st.subheader("Top 10 Municípios com mais acidentes")
top_cidades = df['municipio'].value_counts().head(10)
st.bar_chart(top_cidades)
