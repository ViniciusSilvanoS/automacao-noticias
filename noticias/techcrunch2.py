import json
import requests

# Função para gravar o JSON no arquivo
def gravar_json(json_noticia):
    with open('noticias.json', 'w', encoding='utf-8') as file:
        json.dump(json_noticia, file, ensure_ascii=False, indent=4)

# Função para ler o JSON do arquivo
def ler_json():
    with open('noticias.json', 'r', encoding='utf-8') as file:
        noticias = json.load(file)
    return noticias

# Função principal
def agenteTechcrunch():
    # URL para request (não utilizada neste exemplo específico)
    url = "https://techcrunch.com/category/artificial-intelligence/"
    response = requests.get(url)
    html = response.content

    # JSON de exemplo (este deve ser seu JSON real)
    # exemplo_json = {
    #     "noticias": [
    #         {
    #             "titulo": "Labor shortages are still fueling growth at automation firms like GrayMatter",
    #             "fonte": "TechCrunch",
    #             "urlNoticia": "https://techcrunch.com/2024/06/20/labor-shortages-are-still-fueling-growth-at-automation-firms-like-graymatter/",
    #             "data": "2024-06-20"
    #         },
    #         {
    #             "titulo": "Pocket FM partners with ElevenLabs to convert scripts into audio content quickly",
    #             "fonte": "TechCrunch",
    #             "urlNoticia": "https://techcrunch.com/2024/06/20/pocket-fm-partners-with-elevenlabs-to-convert-scripts-into-audio-content-quickly/",
    #             "data": "2024-06-20"
    #         },
    #         {
    #             "titulo": "Anthropic claims its latest model is best-in-class",
    #             "fonte": "TechCrunch",
    #             "urlNoticia": "https://techcrunch.com/2024/06/20/anthropic-claims-its-latest-model-is-best-in-class/",
    #             "data": "2024-06-20"
    #         },
    #         {
    #             "titulo": "Materia looks to make accountants more efficient with AI",
    #             "fonte": "TechCrunch",
    #             "urlNoticia": "https://techcrunch.com/2024/06/20/materia-looks-to-make-accountants-more-efficient-with-ai/",
    #             "data": "2024-06-20"
    #         },
    #         {
    #             "titulo": "Amazon extends generative AI-powered product listings to Europe",
    #             "fonte": "TechCrunch",
    #             "urlNoticia": "https://techcrunch.com/2024/06/20/amazon-extends-generative-ai-powered-product-listings-to-europe/",
    #             "data": "2024-06-20"
    #         }
    #     ]
    # }

    # Gravando o JSON de exemplo no arquivo
    # gravar_json(exemplo_json)

    # Lendo o JSON do arquivo
    noticias = ler_json()

    # Exibindo as URLs das notícias
    for noticia in noticias["noticias"]:
        print(noticia["urlNoticia"])

# Chamando a função principal
agenteTechcrunch()
