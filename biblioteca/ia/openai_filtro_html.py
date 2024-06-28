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
                {"role": "system", "content": f"Responsável por captar infomações de um arquivo html e retornar no formato json. Sempre responder no idioma português do Brasil. "},
                {"role": "user", "content": f'Capte as informações do arquivo HTML e retorne no formato json com a URL em formato absoluto.'
                                            f'\nCaptar todas noticias presentes no HTML.'
                                            f'\nDesconsidere o tópico da página como um título. Foque apenas nas notícias específicas.'
                                            f'\nResponda SEMPRE em PORTUGUÊS brasileiro, caso esteja inglês, traduza para português.'
                                            f'\nHTML: \n{html}\n\nUse o template a seguir: {schema}\n'
                                            f'\n- titulo: Deve ser pego o tópico da notícia. E sempre ser em português, caso esteja em outro idioma, traduza para o português brasil.'
                                            f'\n- fonte: Deve fornecer a fonte do site que está sendo acessado.'
                                            f'\n- urlNoticia: Deve ser pego a URL absoluta do titulo em específico. A URL que direciona para a notícia completa.'
                                            f'\n- data: Deve pegar a data da postagem da notícia. Caso não tenha, utilizar o dia de hoje, dia {data_alema}\n'
                                            f'\n{prompt_extra}'}
                # {"role": "user", "content": f"Olá json!"}
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