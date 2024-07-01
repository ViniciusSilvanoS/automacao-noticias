import json

from biblioteca.enviar_email import enviar_email
from noticias.captar_noticias import captar_noticias_site
from biblioteca.ia.openai_melhores_noticas import ia_escolher_noticias
from noticias.techcrunch import techcrunch_ia
from noticias.techcrunch import techcrunch_seguranca
from noticias.baguete import baguete
from noticias.businessinsider import *
from noticias.techspot import techspot
from noticias.theverge import *
from noticias.thehackernews import thehackernews
from noticias.canaltech import *
from noticias.microsoft import *
from noticias.dell import dell

# link_noticias = [
#     "https://techcrunch.com/category/artificial-intelligence/",
#     "https://www.baguete.com.br/noticias"
# ]

# link_noticias = [
#    "https://www.baguete.com.br/noticias"
# ]

# noticias = []
# if link_noticias:
#     for link in link_noticias:
#         resultado = captar_noticias_site(link)
#         if resultado:
#             noticias += resultado
noticias = []
# funcoes = [techcrunch_ia, techcrunch_seguranca, baguete, businessinsider_empresa, businessinsider_inovacao, businessinsider_ia, theverge_ia, theverge_tecnologia, thehackernews]
funcoes = [canaltech_notebook, canaltech_corporativo, microsoft,  microsoft_x, dell]
# funcoes = [techcrunch_ia, techcrunch_seguranca, baguete]
# funcoes = [techcrunch_seguranca]
# funcoes = [businessinsider_empresa, businessinsider_inovacao, businessinsider_ia]
# funcoes = [theverge_ia, theverge_tecnologia]
# funcoes = [thehackernews]


# Adicionando prints para rastrear chamadas de função
print("Iniciando a coleta de notícias...")
for func in funcoes:
    print(f"Chamando função: {func.__name__}")
    resultado = func()
    if resultado:
        noticias += resultado
    print(f"Resultado da função {func.__name__}: {resultado}")

print("Resultado do captar noticias: ")
print(noticias)

# Filtra as melhores noticias
noticias_para_filtro = []
for item in noticias:
    id = item["id"]
    titulo = item["titulo"]
    resumoNoticia = item["resumoNoticia"]
    noticias_para_filtro.append({"id": id, "titulo": titulo, "resumoNoticia": resumoNoticia})

print("Noticias com ID: ")
print(noticias_para_filtro)


id_melhores_noticias = ia_escolher_noticias(noticias_para_filtro, 5)

print("id_melhores_noticias: ")
print(id_melhores_noticias)

melhores_noticias = []
teste = json.loads(id_melhores_noticias)
for chave, valor in teste.items():
    print("Valor dentro do for id_melhores_noticias")
    print(valor)
    for noticia in noticias:
        if noticia["id"] == valor:
            melhores_noticias.append(noticia)

print("Notícias filtradas: ")
print(melhores_noticias)

quer_enviar_email = input("Deseja enviar as noticias por email?\n1 para SIM, ou outro valor para NÃO.")
if quer_enviar_email == "1":
    enviar_email(melhores_noticias)
    print("Finalizado!!!")
else:
    print("Não foi enviado email!")

# else:
#     print("Array com links dos sites de noticias está vazio!")

