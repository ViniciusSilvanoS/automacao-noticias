from biblioteca.data import data_alema
from biblioteca.ia.openai_resumo import ia_resumir_texto

def add_data_e_resumo(noticia, html):
    noticia["createdOn"] = data_alema()
    noticia["resumoNoticia"] = (ia_resumir_texto(html))