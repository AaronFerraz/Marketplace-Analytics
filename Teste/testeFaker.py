"""
Projeto simples para estudo do funcionamento de:
- Faker
- pandas
- streamlit

Design Pattern: singleton
"""


import sqlite3
import streamlit as st
import pandas as pd
from faker import Faker

fake = Faker("pt-br")
DB = "empresa.db"


def getConnection(nameDB):
    conn = None

    if not conn:
        conn = sqlite3.connect(nameDB, timeout=30)
        cursor = conn.cursor()
    
    return conn, cursor


def createTableUsuarios():
    _, cursor = getConnection(DB)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            data_nascimento DATE,
            cidade TEXT         
        )
    """)

    print("Tabela 'Usuários' criada ou já existente.")


def insertRandomUser(quantity):
    try:        
        conn, cursor = getConnection(DB)

        users = [ (fake.name(), fake.email(), fake.date_of_birth(minimum_age=18, maximum_age=70), fake.city()) for _ in range(quantity) ]

        cursor.executemany(
            "INSERT INTO usuarios (nome, email, data_nascimento, cidade) VALUES (?, ?, ?, ?)", users
        )

        conn.commit()
        print(f"{cursor.rowcount} usuários foram inseridos com sucesso!")
    except sqlite3.Error as e:
        ...


def insertUser(*args):
    try:
        conn, cursor = getConnection(DB)

        users = [ args ]

        cursor.executemany(
            "INSERT INTO usuarios (nome, email, data_nascimento, cidade) VALUES (?, ?, ?, ?)", users
        )

        conn.commit()
        print(f"{cursor.rowcount} usuários foram inseridos com sucesso!")
    except sqlite3.Error as e:
        ...



def showData():
    conn, _ = getConnection(DB)
    df = pd.read_sql_query("SELECT * FROM usuarios", conn)
    
    st.metric("Total de Usuários", len(df))

    st.dataframe(
        df,
        width='stretch',
        hide_index=True,
        column_config={
            "id": "ID",
            "nome": "Nome",
            "email": "E-mail",
            "data_nascimento": "Data_Nascimento" 
        }
    )

def cleanTable():
    conn, cursor = getConnection(DB)
    cursor.execute("""
        DELETE FROM usuarios;
    """)

    conn.commit()
    print(f"{cursor.rowcount} usuários foram excluídos com sucesso!")


st.title("DataBases Manipualtions")

nome = st.text_input("Escreva um nome: ")
email = st.text_input("Digite seu email: ")
data_nascimento = st.text_input("Digite sua data de nascimento: ")
cidade = st.text_input("Digite sua cidade: ")
if st.button("Inserir usuário"):
    if nome and email and data_nascimento and cidade:
        insertUser(nome, email, data_nascimento, cidade)

quantidade = st.text_input("Digite uma quantidade de novos usuários: ")

col1, col2 = st.columns(2)

with col1:
    if st.button("Inserir x usuários Aleatórios"):
        if quantidade:
            insertRandomUser(int(quantidade))

with col2:
    if st.button("Limpar BD"):
        cleanTable()

if st.button("Mostrar Banco de Dados"):
    showData()