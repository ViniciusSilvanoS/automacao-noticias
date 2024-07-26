import requests

from biblioteca.filtrar_html import limpar_html_com_imagem
from biblioteca.filtrar_html import limpar_html_sem_imagem

def captar_conteudo_url_sem_filtro(url):
    url = "https://www.baguete.com.br/noticias"
    response = requests.get(url)
    html = response.content
    html_limpo = limpar_html_com_imagem(html)
    return html_limpo

def captar_conteudo_url_com_imagem(url):
    url = "https://www.baguete.com.br/noticias"
    response = requests.get(url)
    html = response.content
    html_limpo = limpar_html_com_imagem(html)
    return html_limpo

def captar_conteudo_url_sem_imagem(url):
    url = "https://www.baguete.com.br/noticias"
    response = requests.get(url)
    html = response.content
    html_limpo = limpar_html_sem_imagem(html)
    return html_limpo