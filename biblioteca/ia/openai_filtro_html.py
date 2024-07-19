import json
import os

from openai import OpenAI
from biblioteca.extrair_json import extrair_json
from biblioteca.data import data_alema

# Essa função retorna um dicionario
def ia_filtro_html_para_json(html, prompt_extra = ""):
    try:
        API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")
        client = OpenAI(api_key=API_KEY_OPENAI)

        schema = {
              "titulo": "",
              "fonte": "",
              "urlNoticia": "",
              "data": "yyyy-mm-dd",
        }
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "Responsável por captar títulos e links de notícias de um arquivo HTML e retornar no formato JSON. Sempre responder no idioma português do Brasil."
                            "\nEvitar notícias de: 1 - celulares, 2 - criptomoedas, 3 - hardware gamer, 4 - propaganda de revendas, 5 - notícias referentes ao próprio site."},
                {"role": "user",
                 "content": f'Capte as informações do arquivo HTML e retorne no formato JSON com a URL em formato absoluto.'
                            f'\nExtraia todas as notícias presentes no HTML, excluindo o tópico da página como título. Foque apenas nas notícias específicas.'
                            f'\nResponda SEMPRE em português brasileiro. Caso esteja em outro idioma, traduza para o português brasileiro.'
                            f'\nHTML: \n{html}\n\nUse o seguinte template: {schema}\n'
                            f'\n- titulo: Deve ser o título da notícia. Se estiver em outro idioma, traduza para o português brasileiro.'
                            f'\n- fonte: Deve fornecer a fonte do site que está sendo acessado.'
                            f'\n- urlNoticia: Deve ser a URL absoluta do título específico. A URL que direciona para a notícia completa. Para considerar se é a (urlNoticia) correta, geralmente a URL terá o mesmo nome da fonte dentro da URL. Ex.: www.[fonte]...'
                            f'\n- data: Deve ser a data da postagem da notícia. Caso não tenha, utilizar o dia de hoje, {data_alema()}.\n'
                            f'\nPegar notícias recentes, no máximo 2 meses atrás, considerando que hoje é dia {data_alema()}.'
                            f'\n{prompt_extra}'}
            ],
            max_tokens=1500,
            response_format={"type": "json_object"},
            temperature=0.9
        )

        print("Retorno dentro da ia fitlro_html: ")
        print(completion.choices[0].message.content)
        dicionario_filtrado = extrair_json(completion.choices[0].message.content)
        return json.loads(dicionario_filtrado)
    except Exception as e:
        print(e)
        return None

# print(filtro_html_para_json())