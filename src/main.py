from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

@app.get("/")
def get_products():
    return { "data" : ["Banana", "arroz", "Feijão", "Salada"] }

@app.get("/products")
def get_products():
    return database()

def database():
    client = MongoClient(f"mongodb+srv://user_empreguetes:hNcWtqSsI30ZBwNl1r@empreguetes.qazwi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    return client


    