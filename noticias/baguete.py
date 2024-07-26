import requests
from biblioteca.ia.openai_filtro_html import ia_filtro_html_para_json
from biblioteca.ia.openai_resumo import ia_resumir_texto
from biblioteca.filtrar_html import limpar_html_sem_imagem
from biblioteca.gerar_hash import fazer_hash
from biblioteca.captar_conteudo_url import captar_conteudo_url_sem_imagem
from biblioteca.data import data_alema
from biblioteca.add_data_e_resumo import add_data_e_resumo

def baguete():
    html_limpo = captar_conteudo_url_sem_imagem("https://www.baguete.com.br/noticias")
    # url = "https://www.baguete.com.br/noticias"
    # response = requests.get(url)
    # html = response.content
    # html_limpo = clean_html(html)

    dicionario_noticia = ia_filtro_html_para_json(html_limpo)

    print(dicionario_noticia)
    for noticia in dicionario_noticia:
        hash_id = fazer_hash(noticia["urlNoticia"])
        noticia["id"] = hash_id

    for noticia in dicionario_noticia:
        url = noticia["urlNoticia"]
        captar_conteudo_url_sem_imagem(url)
        # response = requests.get(url)
        # html = response.content
        # html_limpo = limpar_html_sem_imagem(html)
        add_data_e_resumo(noticia, html_limpo)
        # noticia["createdOn"] = data_alema()
        # noticia["resumoNoticia"] = (ia_resumir_texto(html_limpo))

    print(dicionario_noticia)
    return dicionario_noticia