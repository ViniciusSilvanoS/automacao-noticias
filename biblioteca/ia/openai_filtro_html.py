import json

from openai import OpenAI
from biblioteca.extrair_json import extrair_json

# Essa função retorna um dicionario
def ia_filtro_html_para_json(html):
    api_key = open("../OPENAI_API_KEY", "r").read()
    client = OpenAI(api_key=api_key)

    schema = {
          "titulo": "",
          "fonte": "",
          "urlNoticia": "",
          "data": "yyyy-mm-dd",
    }
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Sou responsável por captar infomações de um arquivo html e retornar no formato json. Sempre responderei no idioma português do Brasil"},
            {"role": "user", "content": f'Capte as informações do arquivo html e retorne no formato json com a URL em formato absoluto. '
                                        f'\nHTML: \n{html}\n\nUse o template a seguir: {schema}\n\nA fonte pedida no template deve ser considerado o nome do site acessado.'}
            # {"role": "user", "content": f"Olá json!"}
        ],
        max_tokens=1500,
        response_format={"type": "json_object"},
        temperature=0.9
    )

    print("Retorno dentro da ia fitlro_html: ")
    print(completion.choices[0].message.content)
    json_filtrado = extrair_json(completion.choices[0].message.content)
    return json.loads(json_filtrado)


# print(filtro_html_para_json())