import pandas as pd
from faker import Faker
from sqlalchemy import create_engine, text
import random
import urllib.parse
from datetime import datetime

# Settings
fake = Faker()

password = "A@ron123"
safe_password = urllib.parse.quote_plus(password)
engine = create_engine(f"mysql+mysqlconnector://root:{safe_password}@localhost/marketplace")


def generate_fake_data(quantity=1_000_000):
    print("Iniciando geração de dados...")

    # ----- Clientes -----
    n_customers = 50000
    customers = [{
        'firstname': fake.first_name(),
        'lastname': fake.last_name(),
        'country': fake.country(),
        'score': random.randint(0, 100)
    } for _ in range(n_customers)]
    pd.DataFrame(customers).to_sql('customers', engine, if_exists='append', index=False)
    print("Clientes inseridos...")

    # ----- Produtos -----
    n_products = 5000
    categories = ['Eletrônicos', 'Moda', 'Casa', 'Beleza', 'Esportes']
    products = [{
        'productname': fake.catch_phrase(),
        'category': random.choice(categories),
        'price': round(random.uniform(50, 5000), 2),
        'cost_price': round(random.uniform(10, 2000), 2),
        'brand': fake.company()
    } for _ in range(n_products)]
    pd.DataFrame(products).to_sql('products', engine, if_exists='append', index=False)
    print('Produtos inseridos...')

    # ----- Funcionários -----
    # Gerentes
    n_managers = 120
    managers = []
    for _ in range(n_managers):
        managers.append({
            'firstname': fake.first_name(),
            'lastname': fake.last_name(),
            'departament': 'Diretoria',
            'birthday': fake.date_of_birth(minimum_age=30, maximum_age=65),
            'gender': random.choice(['M', 'F']),
            'salary': round(random.uniform(9000, 16000), 2),
            'managerID': None
        })

    pd.DataFrame(managers).to_sql('employees', engine, if_exists='append', index=False)

    with engine.begin() as conn:
        result_manager = conn.execute(text("SELECT id FROM employees WHERE departament = 'Diretoria'")) 
        manager_ids = [row[0] for row in result_manager]

        # Empregados
        n_employees = 1000
        employees = []
        for _ in range(n_employees):
            employees.append({
                'firstname': fake.first_name(),
                'lastname': fake.last_name(),
                'departament': 'Vendas',
                'birthday': fake.date_of_birth(minimum_age=20, maximum_age=60),
                'gender': random.choice(['M', 'F']),
                'salary': round(random.uniform(3000, 12000), 2),
                'managerID': random.choice(manager_ids)
            })
    
        df_emp = pd.DataFrame(employees)
        df_emp.to_sql('employees', engine, if_exists='append', index=False)

        customer_ids = [row[0] for row in conn.execute(text("SELECT id FROM customers"))]
        products_ids = [row[0] for row in conn.execute(text("SELECT id FROM products"))]
        employees_ids = [row[0] for row in conn.execute(text("SELECT id FROM employees WHERE departament = 'Vendas'"))]

    if not employees_ids:
        raise ValueError("ERRO: a lista de vendedores est" \
        "a vazia.")


    # ----- Pedidos -----
    chunk_size = 50_000
    today = datetime.now()

    for i in range(0, quantity, chunk_size):
        orders = []
        for _ in range(chunk_size):
            price = random.uniform(50, 5000)
            qty = random.randint(1, 5)
            orders.append({
                'product_id': random.choice(products_ids),
                'customer_id': random.choice(customer_ids),
                'salesperson_id': random.choice(employees_ids),
                'orderdate': fake.date_between(start_date='-2y', end_date=today),
                'quantity': qty,
                'sales': round(price * qty, 2),
                'payment_method': random.choice(['Cartão de Crédito', "Pix", "Boleto"]),
                'orderstatus': random.choice(['Enviado', 'Em Espera', 'Pendente']),
                'creationtime': fake.date_time_between(start_date='-2y', end_date=today)
            })

        df_orders = pd.DataFrame(orders)
        df_orders.to_sql('orders', engine, if_exists='append', index=False)
        print(f'Bloco de {i + chunk_size} pedidos inseridos...')



generate_fake_data(1_000_000)