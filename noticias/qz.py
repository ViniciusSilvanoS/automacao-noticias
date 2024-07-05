import requests
from biblioteca.ia.openai_filtro_html import ia_filtro_html_para_json
from biblioteca.ia.openai_resumo import ia_resumir_texto
from biblioteca.filtrar_html import clean_html
from biblioteca.gerar_hash import fazer_hash

prompt = ""
def qz_empresas():
    url = "https://qz.com/business-news"
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
    return dicionario_noticia

def qz_ia():
    url = "https://qz.com/business-news/generation-ai"
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
    return dicionario_noticia

def qz_lideranca():
    url = "https://qz.com/leadership"
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
    return dicionario_noticia