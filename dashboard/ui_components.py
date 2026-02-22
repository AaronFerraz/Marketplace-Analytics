'''
Este módulo contém funções que são responsáveis por desenhar partes específicas da interface.
O que faz? Cria os gráficos, tabelas e cartões de KPI. Recebe um DataFrame como argumento e usa os comandos do Streamlit (st.bar_chart, st.metric, st.plotly_chart) para renderizar a visualização.
Como implementar? Use funções simples, não classes. Cada função é um "widget" de UI reutilizável.
'''

import streamlit as st
import matplotlib.pyplot as plt


def plot_category_sales(df):
    st.subheader("Faturamento por Categoria")
    fig, ax = plt.subplots()
    ax.bar(df['category'], df['total_sales'], color='skyblue')
    ax.set_ylabel("Vendas (R$)")
    plt.xticks(rotation=45)
    st.pyplot(fig)


def plot_time_series(df):
    st.subheader("Evolução das Vendas no Tempo")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df['orderdate'], df['daily_sales'], color="green", linewidth=1)
    ax.set_xlabel('Data')
    ax.set_ylabel("Vendas Diárias")
    plt.grid(True, alpha=0.3)
    st.pyplot(fig)