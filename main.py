import json

from biblioteca.enviar_email import email_diario
from biblioteca.enviar_email import email_marketing
from biblioteca.ia.openai_melhores_noticas import ia_escolher_noticias
from noticias.baguete import baguete
from biblioteca.ia.openai_captar_imagem import ia_captar_imagem_site
from biblioteca.ia.openai_gerar_imagem import ia_fazer_imagem
from repositorio.noticias_repositorio import adicionar_noticias

noticias = []
# funcoes = [techspot, techcrunch_ia, techcrunch_seguranca, baguete, businessinsider_empresa, businessinsider_inovacao, businessinsider_ia, theverge_ia, theverge_tecnologia, thehackernews, canaltech_notebook, canaltech_corporativo, dell, ingram_ti, ingram_cloud, mit]
# funcoes = [canaltech_notebook, canaltech_corporativo, microsoft,  microsoft_x, dell, adobe]
# funcoes = [ingram_ti, ingram_cloud, scansource]
# funcoes = [techcrunch_ia, techcrunch_seguranca, baguete]
funcoes = [baguete]
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

# Captando noticias de cada site
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

# Escolhe a melhor noticia
id_melhores_noticias = ia_escolher_noticias(noticias_para_filtro, 5)

melhores_noticias = []
teste = json.loads(id_melhores_noticias)
for chave, valor in teste.items():
    # print("Valor dentro do for id_melhores_noticias")
    print(valor)
    for noticia in noticias:
        if noticia["id"] == valor:
            melhores_noticias.append(noticia)

print("Notícias filtradas: ")
print(melhores_noticias)

# Gerar e salvar imagem na noticia
# for noticia in melhores_noticias:
#     id_imagem = ia_fazer_imagem(noticia['titulo'], noticia['resumoNoticia'])
#     if id_imagem is not None:
#         noticia["idImagem"] = id_imagem
#     else:
#         print("Erro ao adicionar imagem.")


# Captando a imagem da noticia
if melhores_noticias:
    for noticia in melhores_noticias:
        ia_captar_imagem_site(noticia['urlNoticia'])


# Adicionando noticias ao banco de dados
# if melhores_noticias:
#     try:
#         adicionar_noticias(melhores_noticias)
#     except Exception as e:
#         print(f"Erro ao adicionar noticias: {e}")

# Fazer email marketing das noticias
# cont = 0
# for noticia in melhores_noticias:
#     cont += 1
#     print(ia_fazer_html_noticia(noticia))
#     email_marketing(ia_fazer_html_noticia(noticia))
#     print(cont + "º email enviado!")



quer_enviar_email = input("Deseja enviar as noticias por email?\n1 para SIM, ou outro valor para NÃO.")
if quer_enviar_email == "1":
    email_diario(melhores_noticias)
    print("Finalizado!!!")
else:
    print("Não foi enviado email!")



