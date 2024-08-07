import json
import requests
from biblioteca.ia.openai_filtro_html import ia_filtro_html_para_json
from biblioteca.ia.openai_resumo import ia_resumir_texto
from biblioteca.filtrar_html import limpar_html_sem_imagem
from biblioteca.gerar_hash import fazer_hash

def venturebeat_ai():
    try:
        url = "https://venturebeat.com/category/ai/"
        response = requests.get(url)
        html = response.content

        html_limpo = limpar_html_sem_imagem(html)

        dicionario_noticia = ia_filtro_html_para_json(html_limpo)

        # print(dicionario_noticia)
        for noticia in dicionario_noticia:
            hash_id = fazer_hash(noticia["urlNoticia"])
            noticia["id"] = hash_id

        for noticia in dicionario_noticia:
            url = noticia["urlNoticia"]
            response = requests.get(url)
            html = response.content
            html_limpo = clean_html(html)
            noticia["resumoNoticia"] = (ia_resumir_texto(html_limpo))

        return dicionario_noticia
    except Exception as e:
        print(e)
        return None

def venturebeat_infraestrutura_de_dados():
    try:
        url = "https://venturebeat.com/category/data-infrastructure/"
        response = requests.get(url)
        html = response.content

        html_limpo = clean_html(html)

        dicionario_noticia = ia_filtro_html_para_json(html_limpo)

        # print(dicionario_noticia)
        for noticia in dicionario_noticia:
            hash_id = fazer_hash(noticia["urlNoticia"])
            noticia["id"] = hash_id

        for noticia in dicionario_noticia:
            url = noticia["urlNoticia"]
            response = requests.get(url)
            html = response.content
            html_limpo = clean_html(html)
            noticia["resumoNoticia"] = (ia_resumir_texto(html_limpo))

        return dicionario_noticia
    except Exception as e:
        print(e)
        return None

def venturebeat_analise_de_empresas():
    try:
        url = "https://venturebeat.com/category/enterprise-analytics/"
        response = requests.get(url)
        html = response.content

        html_limpo = clean_html(html)

        dicionario_noticia = ia_filtro_html_para_json(html_limpo)

        # print(dicionario_noticia)
        for noticia in dicionario_noticia:
            hash_id = fazer_hash(noticia["urlNoticia"])
            noticia["id"] = hash_id

        for noticia in dicionario_noticia:
            url = noticia["urlNoticia"]
            response = requests.get(url)
            html = response.content
            html_limpo = clean_html(html)
            noticia["resumoNoticia"] = (ia_resumir_texto(html_limpo))

        return dicionario_noticia
    except Exception as e:
        print(e)
        return None

def venturebeat_automacao():
    try:
        url = "https://venturebeat.com/category/automation/"
        response = requests.get(url)
        html = response.content

        html_limpo = clean_html(html)

        dicionario_noticia = ia_filtro_html_para_json(html_limpo)

        # print(dicionario_noticia)
        for noticia in dicionario_noticia:
            hash_id = fazer_hash(noticia["urlNoticia"])
            noticia["id"] = hash_id

        for noticia in dicionario_noticia:
            url = noticia["urlNoticia"]
            response = requests.get(url)
            html = response.content
            html_limpo = clean_html(html)
            noticia["resumoNoticia"] = (ia_resumir_texto(html_limpo))

        return dicionario_noticia
    except Exception as e:
        print(e)
        return None