from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://juliovicente:BJBJTcCZ7UjoQxfG@cluster0.ge3eqjy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))

database = client["marketing_noticias"]
collection = database["noticias"]

def is_duplicado(noticia):
    results = collection.find_one({"id": noticia['id']})
    return results
def adicionar_noticias(noticias):
    for noticia in noticias:
        if not is_duplicado(noticia):
            collection.insert_one(noticia)
            print("Adicionado!")

