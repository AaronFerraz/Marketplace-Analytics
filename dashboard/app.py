'''
A Aplicação Principal (Controller/Orchestrator): app.py
Este é o seu script principal, o ponto de entrada. Ele é o "maestro" que orquestra as outras duas camadas.

O que faz?
Configura a página (st.set_page_config).
Renderiza os widgets de controle (filtros, sliders, botões), geralmente na barra lateral (st.sidebar).
Chama a camada de dados para carregar e filtrar os dados com base na entrada do usuário.
Chama as funções da camada de visualização para exibir os resultados.
Gerencia o estado da aplicação com st.session_state.
'''


import streamlit as st
from data_services import DataModel
import pandas as pd
import ui_components as view

st.set_page_config(page_title="Marketplace Analytics", layout="wide")

@st.cache_data
def load_data():
    model = DataModel()
    cat_data = model.get_sales_by_category()
    time_data = model.get_sales_over_time()
    return cat_data, time_data

st.title("Dashboard de Venda - Marketplace")
st.sidebar.header("Filtros")
filtro_exemplo = st.sidebar.multiselect("Selecione Categorias", ['Eletrônicos', 'Moda', 'Casa', 'Beleza', 'Esportes'])

cat_df, time_df = load_data()

col1, col2 = st.columns(2)

with col1:
    view.plot_category_sales(cat_df)

with col2: 
    view.plot_time_series(time_df)


st.divider()
st.dataframe(cat_df, use_container_width=True)