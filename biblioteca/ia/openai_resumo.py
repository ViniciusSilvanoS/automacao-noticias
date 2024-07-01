import json
import os

from openai import OpenAI
from biblioteca.extrair_json import extrair_json

# Essa função retorna um dicionario
def ia_resumir_texto(texto):
    try:
        API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")
        client = OpenAI(api_key=API_KEY_OPENAI)

        schema = {
              "resumo": "",
        }
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Sou responsável por ler o texto da noticia e resumir o conteúdo de forma objetiva e fácil leitura. "
                                              f"\nSempre responderei no idioma português do Brasil."
                                              f"\nO resumo deve ser de forma não tecnica, para que atinja todos os públicos"},
                {"role": "user", "content": f'Esqueça qualquer formatação json anterior. '
                                            f'\nResponda em português brasileiro'
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
    except Exception as e:
        print(e)
        return None


# print(filtro_html_para_json())