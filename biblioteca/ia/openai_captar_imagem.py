import json
import os

from openai import OpenAI
from biblioteca.extrair_json import extrair_json
from biblioteca.data import data_alema
from biblioteca.captar_conteudo_url import captar_conteudo_url_com_imagem

# Essa função retorna um dicionario
def ia_captar_imagem_site(url):
    try:
        API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")
        client = OpenAI(api_key=API_KEY_OPENAI)

        print("URL recebida")
        print(url)

        html_limpo = captar_conteudo_url_com_imagem(url)

        print(html_limpo)

        schema = {
              "urlImagem": "",
        }

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "Responsável por captar a imagem que corresponde ao conteúdo da notícia"},
                {"role": "user",
                 "content": f'Extraia o link da imagem usada para ilustrar a noticia.'
                            f'\nDica: Geralmente o link da imagem está em src dentro da tag <img>, ou dentro da tag url em uma <div>'
                            f'\nCapte a imagem deste html: {html_limpo}\n'
                            f'\nRetorne em json, seguindo o template: {schema}'}
            ],
            max_tokens=1500,
            response_format={"type": "json_object"},
            temperature=0.9
        )

        print("Retorno dentro da ia captar_imagem: ")
        dicionario_filtrado = extrair_json(completion.choices[0].message.content)
        print(dicionario_filtrado)
        return json.loads(dicionario_filtrado)
    except Exception as e:
        print(e)
        return None

# print(filtro_html_para_json())