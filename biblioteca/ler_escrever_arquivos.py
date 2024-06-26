import json


def gravar_json(json_noticia, local):
    with open(local, 'w', encoding='utf-8') as file:
        json.dump(json_noticia, file, ensure_ascii=False, indent=4)

def ler_json(local):
    with open(local, 'r', encoding='utf-8') as file:
        noticias = json.load(file)
    return noticias