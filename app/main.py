from fastapi import FastAPI
import uvicorn # Cria servidor llocal no computador
from datetime import date

data = str(date.today())

app = FastAPI()

info = {
    'name' : 'In Gnave',
    'id': '01',
    'last_access': data
}


@app.get('/') #decorator
def home():
    return 'Seja bem Vindo ao Banco Mock ;)'

@app.get('/about') #decorator
def about():
    return 'Nós somos Banco Mock'

@app.get('/user') #decorator
def get_users():
    return info


if __name__ == '__main__':
    uvicorn.run(app = app, port=8080)