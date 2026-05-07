from fastapi import FastAPI
from database import get_db

app = FastAPI()

@app.get("/")
def rota():
    print(get_db())
    return("rota funcionando :)")
