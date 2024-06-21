import hashlib
import json
from bs4 import BeautifulSoup as bs
import requests
from biblioteca.ia.openai_filtro_html import ia_filtro_html_para_json
from biblioteca.ia.openai_resumo import ia_resumir_texto
from biblioteca.filtrar_html import clean_html
from biblioteca.extrair_json import extrair_json

def fazer_hash(valor):
    hash = hashlib.sha256(valor.encode()).hexdigest()
    return hash

def gravar_json(json_noticia):
    with open('noticias.json', 'w', encoding='utf-8') as file:
        json.dump(json_noticia, file, ensure_ascii=False, indent=4)

def ler_json():
    with open('noticias.json', 'r', encoding='utf-8') as file:
        noticias = json.load(file)
    return noticias

def techcrunch():
    url = "https://techcrunch.com/category/artificial-intelligence/"
    response = requests.get(url)
    html = response.content

    html_limpo = clean_html(html)

    dicionario_noticia = ia_filtro_html_para_json(html_limpo)

    print(dicionario_noticia)
    for noticia in dicionario_noticia:
        hash_id = fazer_hash(noticia["urlNoticia"])
        noticia["id"] = hash_id

    for noticia in dicionario_noticia:
        url = noticia["urlNoticia"]
        response = requests.get(url)
        html = response.content
        html_limpo = clean_html(html)
        noticia["resumoNoticia"] = (ia_resumir_texto(html_limpo))

    print(dicionario_noticia)



techcrunch()