from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Operadora, Protocolo

app = FastAPI()

# rota para listar operadoras
@app.get("/operadoras")
def listar_operadoras(db: Session = Depends(get_db)):
    return db.query(Operadora).all()

# rota para listar protocolos de uma operadora
@app.get("/operadoras/{operadora_id}/protocolos")
def listar_protocolos_por_operadora(
    operadora_id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(Protocolo)
        .filter(Protocolo.operadora_id == operadora_id)
        .all()
    )