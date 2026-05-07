# models.py

# aqui estou importando a biblioteca inteira
import sqlalchemy as sa

# o relationship cria um relacionamento orm entre tabelas, permitindo acessar dados relacionados sem usar sql
from sqlalchemy.orm import relationship

# aqui estamos importando Base a fim de que as models façam sentido e funcionem
from database import Base

# crio uma classe para as tabela operadoras dando a herança de (Base)
class Operadora(Base): 
    __tablename__ = "operadoras"

    id = sa.Column(sa.Integer, primary_key=True)
    nome = sa.Column(sa.String(100), nullable=False, index=True)

    protocolos = relationship("Protocolo", back_populates="operadora") # relacionamento dentro da classe

# crio uma classe para as tabela protocolo dando a herança de (Base)
class Protocolo(Base):
    __tablename__ = "protocolos"

    id = sa.Column(sa.Integer, primary_key=True)
    numero = sa.Column(sa.String(50), nullable=False, index=True)
    data_criacao = sa.Column(sa.DateTime, nullable=True, index=True)
    operadora_id = sa.Column(sa.Integer, sa.ForeignKey("operadoras.id"), nullable=False, index=True) # isso é uma foreign key (fk), veio de operadora

    operadora = relationship("Operadora", back_populates="protocolos")







