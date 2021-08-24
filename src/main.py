from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_products():
    return { "data" : ["Banana", "arroz", "Feijão", "Salada"] }
