import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def a():
    dados = {
        'Nome': ['Aaron F', 'Joana', 'Maria', 'Josefa', 'Lucas', 'Aaron B'],
        'Idade': [25, 30, 35, 28, 14, None],
        'Cidade': ['SP', 'RJ', 'BH', 'SP', 'PR', 'MG']
    }

    df = pd.DataFrame(dados)
    print(df)

    print(df.columns)
    print(df.index)
    print(df.tail(1))
    print(df.sample(2))
    print(df.info())

    print(df.describe(include='all'))
    print(df.isnull().sum())
    print(df['Nome'].value_counts(normalize=True))

    df_filtrado = df.fillna(0)
    print(df_filtrado)

    print("quatro linhas: \n", df.loc[0:3, 'Nome'])

    print()

    df = pd.DataFrame(columns=["Name", "Team", "Number"])
    df.loc[0] = ["Aaron", "Vapo", "1234"]

    series1 = pd.Series(df['Name'])
    series2 = pd.Series(df['Team'])
    series3 = pd.Series(df['Number'])

    print(df)
    print(series1)
    print(series2)
    print(series3)


    # df3 = pd.read_clipboard()
    # print(df3['cotacao'])


    # tabelas = pd.read_html('https://investidor10.com.br/acoes/rankings/maiores-valor-de-mercado/')

    # df4 = tabelas[0]
    # df4.to_json('./acoes.json', indent=4)


def b():
    # Gráfico de linha simples
    np.random.seed(42)
    df = pd.DataFrame({
        'vendas': np.random.normal(1000, 200, 100),
        'clientes': np.random.poisson(50, 100),
        'tempo_site': np.random.poisson(300, 100),
        'mes': range(1, 101),
    })

    df.plot.line(x='mes', y='vendas', 
             title='Vendas ao Longo do Tempo',
             figsize=(10, 6),
             grid=True,
             color='red',
             linewidth=2)
    plt.ylabel('Vendas (R$)')
    plt.show()

    # Criar subplots com pandas
    axes = df[['vendas', 'clientes', 'tempo_site']].plot(
        kind='hist',
        subplots=True,
        figsize=(12, 8),
        bins=15,
        alpha=0.7,
        edgecolor='black',
        layout=(1, 3)  # 1 linha, 3 colunas
    )

    plt.suptitle('Distribuições das Variáveis', fontsize=16)
    plt.tight_layout()
    plt.show()



a()


 