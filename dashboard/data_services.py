'''
Aqui é onde as classes fazem mais sentido. Esta camada é responsável por toda a lógica de acesso e manipulação de dados.
O que faz? Conecta-se a bancos de dados, carrega arquivos CSV/Excel, chama APIs, e realiza as transformações e cálculos pesados com Pandas/NumPy.
Como implementar? Crie uma classe ou um conjunto de funções que retornem DataFrames limpos e prontos para uso. O importante é que esta camada não sabe nada sobre o Streamlit. Ela apenas lida com dados.

toda Session criada pelo SessionLocal pede uma conexão ao Engine
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import pandas as pd
import urllib.parse



class DataModel:
    def __init__(self):
        self.password = urllib.parse.quote_plus("A@ron123")
        self.url = f"mysql+mysqlconnector://root:{self.password}@localhost:3306/marketplace"
        self.engine = create_engine(self.url)


    def get_sales_by_category(self):
        query = """
            SELECT category, SUM(sales) as total_sales
            FROM products p
            JOIN orders o ON p.id = o.product_id
            GROUP BY category
        """ 
        return pd.read_sql(query, self.engine)

    def get_sales_over_time(self):
        query = """
            SELECT orderdate, SUM(sales) as daily_sales
            FROM orders
            GROUP BY orderdate
            ORDER BY orderdate
        """
        df = pd.read_sql(query, self.engine)
        df['orderdate'] = pd.to_datetime(df['orderdate'])
        return df




# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()



if __name__ == "main":
    ...