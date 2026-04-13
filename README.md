# API Base | Isadora

## Requisitos
- Python 3.x
- pip

## Como rodar:

### 1. Crie e ative o ambiente virtual

python -m venv venv

venv\Scripts\activate

### 2. Instale as dependências

pip install -r requirements.txt

### 3. Rode a API

uvicorn main:app --reload

### 4. Acesse
- API: http://127.0.0.1:8000
- Documentação: http://127.0.0.1:8000/docs