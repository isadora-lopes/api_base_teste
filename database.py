import os # o os é um módulo nativo do python que permite que vc use variáveis de ambiente, interaja com o ambiente operacional, manipular arquivos e etc

import sqlalchemy as sa # importo o sqlalchemy com o apelido de sa que nem nas models
import sqlalchemy.orm as orm # importo o módulo orm 
from dotenv import load_dotenv  # importo o load_dotenv que vai ler o arquivo .env e carregar as variáveis de lá (senha do banco, etc)

load_dotenv() # essa função lê o arquivo .env

DB_URL = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"


engine = sa.create_engine(DB_URL) # o engine pega o endereço declarado e faz a conexão acontecer (faz parte do sqlalchemy)
SessionLocal = orm.sessionmaker(bind=engine) # abre sessões novas
Base = orm.declarative_base() # é a classe mãe de todos os models

def get_db(): # é uma função que abre a sessão no bd, entrega e fecha 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# isso daqui foi adicionado apenas para testar a conexão com o banco
if __name__ == "__main__":
    try:
        conn = engine.connect()
        print("Conexão bem sucedida!")
        conn.close()
    except Exception as e:
        print(f"Erro: {e}")