from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def rota():
    return("rota funcionando :)")