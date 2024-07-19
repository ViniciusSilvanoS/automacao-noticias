import gridfs
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://juliovicente:BJBJTcCZ7UjoQxfG@cluster0.ge3eqjy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))

database = client["marketing_noticias"]
collection = database["noticias"]
fs = gridfs.GridFS(database)

def is_duplicado(noticia):
    results = collection.find_one({"id": noticia['id']})
    return results
def adicionar_noticias(noticias):
    for noticia in noticias:
        if not is_duplicado(noticia):
            collection.insert_one(noticia)
            print("Adicionado!")

def adicionar_imagem(request_imagem, nome):
    image_id = fs.put(request_imagem.content, filename=nome)
    print("ID da imagem: ", image_id)
    return image_id
