from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

produtos = [{
    "id":1,
    "nome":"Iphone14",
    "descricao": "Celular da Apple",
    "preco": 5000.00
},
{
    "id":2,
    "nome":"PS5",
    "descricao": "Video Game da Sony",
    "preco": 2000.00
},
{
    "id":3,
    "nome":"Workshop",
    "descricao": "Workshop do jupyter pro deploy",
    "preco": 120.00
},
]

@app.get("/produtos")
def retorna_lista_produtos():
    return produtos