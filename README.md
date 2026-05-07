# segue passo a passo de como rodar essa api

## requisitos
- Python 3.x
- pip

## como rodar:

### 1. crie e ative o ambiente virtual

python -m venv venv

venv\Scripts\activate

### 2. instale as dependências

pip install -r requirements.txt

### 3. rode a API

uvicorn main:app --reload

### 4. acesse
- API: http://127.0.0.1:8000
- Documentação: http://127.0.0.1:8000/docs
