from biblioteca.enviar_email import enviar_email
from biblioteca.ia.openai_melhores_noticas import ia_escolher_noticias
from noticias.venturebeat import *
from noticias.qz import *
from noticias.nao_funcionaram.adobe import adobe
from noticias.nao_funcionaram.microsoft import *
from noticias.nao_funcionaram.scansource import scansource
from noticias.nao_funcionaram.searchengineland import searchengineland
from noticias.nao_funcionaram.theregister import theregister
from noticias.aruba import aruba
from noticias.custumer import custumer
from noticias.techcrunch import *
from noticias.baguete import baguete
from noticias.businessinsider import *
from noticias.theverge import *
from noticias.thehackernews import thehackernews
from noticias.canaltech import *
from noticias.dell import dell
from noticias.distribuidoras.ingram import *
from noticias.mit import mit
from noticias.techspot import techspot

noticias = []
# funcoes = [techspot, techcrunch_ia, techcrunch_seguranca, baguete, businessinsider_empresa, businessinsider_inovacao, businessinsider_ia, theverge_ia, theverge_tecnologia, thehackernews, canaltech_notebook, canaltech_corporativo, dell, ingram_ti, ingram_cloud, mit]
# funcoes = [canaltech_notebook, canaltech_corporativo, microsoft,  microsoft_x, dell, adobe]
# funcoes = [ingram_ti, ingram_cloud, scansource]
funcoes = [techcrunch_ia, techcrunch_seguranca, baguete]
# funcoes = [techcrunch_seguranca]
# funcoes = [businessinsider_empresa, businessinsider_inovacao, businessinsider_ia]
# funcoes = [theverge_ia, theverge_tecnologia]
# funcoes = [thehackernews]
# funcoes = [theregister]
# funcoes = [mit]
# funcoes = [convergenciadigital]
# funcoes = [aruba]
# funcoes = [venturebeat_ai, venturebeat_automacao, venturebeat_infraestrutura_de_dados, venturebeat_analise_de_empresas]
# funcoes = [searchengineland]
# funcoes = [qz_ia, qz_empresas, qz_lideranca, venturebeat_ai, venturebeat_automacao, venturebeat_infraestrutura_de_dados, venturebeat_analise_de_empresas]
# funcoes = [adobe, microsoft, microsoft_x, scansource, searchengineland, theregister]
# funcoes = [custumer]

# Adicionando prints para rastrear chamadas de função
print("Iniciando a coleta de notícias...")
for func in funcoes:
    try:
        print(f"Chamando função: {func.__name__}")
        resultado = func()
        if resultado:
            noticias += resultado
        print(f"Resultado da função {func.__name__}: {resultado}")
    except Exception as e:
        print(f"Erro ao executar a função {func.__name__}: {e}")

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

# Parei aqui
for melhores_noticias:


quer_enviar_email = input("Deseja enviar as noticias por email?\n1 para SIM, ou outro valor para NÃO.")
if quer_enviar_email == "1":
    enviar_email(melhores_noticias)
    print("Finalizado!!!")
else:
    print("Não foi enviado email!")

