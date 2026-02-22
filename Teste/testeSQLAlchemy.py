'''
Vídeo base: https://www.youtube.com/watch?v=7xQhlf8qnsE

ORM (Object-Relational Mapping)
- Permite trabalhar com BDs utilizando classes e objetos na linguagem de programação.

Abstração do SQL - permite manipular dados do BD sem uso do SQL
Portabilidade - não fica amarrado a um SGBD específico.
Suporte a consultas complexas
Controle transacional:
- commit
- rollback
Permite utilizar SQL


CRUD com o SQLAlchemy:
'''

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer

# configurando a engine do BD
engine = create_engine("sqlite:///database.db")

# configurando a sessão
Session = sessionmaker(engine)

# criando a tabela
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    tipo = Column(String, nullable=False)


# Inserir
def insert_usuario(nome_usuario, tipo_usuario):
    session = Session()

    try:
        if all([nome_usuario, tipo_usuario]):
            usuario = Usuario(nome=nome_usuario, tipo=tipo_usuario)
            session.add(usuario)
            session.commit()
            print(f'Usuário {nome_usuario} cadastrado com sucesso')
        else:
            print('É obrigatório preencher o nome e o tipo do usuário.')
    except Exception as e:
        session.rollback()
        print(f'Ocorreu um erro ao tentar cadastrar o usuário {nome_usuario}:  {e}')
    finally:
        session.close()


# Consultar
def select_usuarios(nome_usuario=''):
    session = Session()
    try:
        if nome_usuario:
            dados = session.query(Usuario).filter(Usuario.nome == nome_usuario)
        else:
            dados = session.query(Usuario).all()

        for i in dados:
            print(f'Usuário: {i.nome} - Tipo: {i.tipo}')

    except Exception as e:
        print('Ocorreu algum erro ao consultar o(s) usuario(s)!')

    finally:
        session.close()


# Atualizar
def update_nome_usuario(id_usuario, nome_usuario):
    session = Session()

    try:
        if all([id_usuario, nome_usuario]):
            usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
            usuario.nome = nome_usuario
            session.commit()
            print('Nome do usuário atualizado com sucesso!')
        else:    
            print('É obrigatório informar o id e o novo nome do usuário')
    except Exception as e:
        session.rollback()
        print('Ocorreu um erro ao atualizar o usuário.')
    finally:
        session.close()
    

# Exclusão

def delete_usuario(id_usuario):
    session = Session()

    try:
        if id_usuario:
            usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
            session.delete(usuario)
            session.commit()
            print(f'Usuário de ID {id_usuario} deletado com sucesso!')
        else:
            print('É obrigatório informar o ID do usuário a ser deletado!')
    except Exception as e:
        session.rollback()
        print(f'Erro ao tentar deletar o usuário de ID {id_usuario}')
    finally:
        session.close()


if __name__ == "__main__":
    os.system('cls')
    Base.metadata.create_all(engine)
    # insert_usuario('Aaron', 'Aluno')
    # insert_usuario('Pedro', 'Professor')
    # insert_usuario('Juliana', 'Administradora')
    # insert_usuario('Maria', 'Monitora')

    select_usuarios()

    # update_nome_usuario(1, 'Joutaro')

    # delete_usuario(4)