from fastapi import FastAPI
import uvicorn

app = FastAPI()


info = {
    'name': 'In Gnave',
    'id': '12345',
    'last_access': '07/08/2022'
}


@app.get('/')
def home():
    return 'Seja Bem Vindo Ao Meu Perfil'


@app.get('/about')
def about():
    return 'Eu sou um cara complexo. Prefiro Linux do que Windows. Se pá, o Mac.'


@app.get('/idade')
def get_users():
    return 28



if __name__ == '__main__':
    uvicorn.run(app=app, port=8080)