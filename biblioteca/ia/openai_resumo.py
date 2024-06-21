import json

from openai import OpenAI
from biblioteca.extrair_json import extrair_json

# Essa função retorna um dicionario
def ia_resumir_texto(texto):
    api_key = open("../OPENAI_API_KEY", "r").read()
    client = OpenAI(api_key=api_key)

    schema = {
          "resumo": "",
    }
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Sou responsável por ler o texto da noticia e resumir. Sempre responderei no idioma português do Brasil"},
            {"role": "user", "content": f'Esqueça qualquer formatação json anterior. '
                                        f'\nNão traga noticias sobre celulares e cripto-moedas.'
                                        f'\nResuma o texto a seguir retornando em formato json, deixando em média um resumo de 100 palavras: {texto}\nUse o template a seguir: {schema}'}
            # {"role": "user", "content": f"Olá json!"}
        ],
        max_tokens=1500,
        response_format={"type": "json_object"},
        temperature=0.9
    )

    print("Retorno dentro da ia resumo: ")
    print(completion.choices[0].message.content)
    json_filtrado = extrair_json(completion.choices[0].message.content)
    return (json.loads(json_filtrado)[0]["resumo"])


# print(filtro_html_para_json())