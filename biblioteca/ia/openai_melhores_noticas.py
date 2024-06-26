from openai import OpenAI
import os
# Essa função retorna um dicionario
def ia_escolher_noticias(noticias_json, qtd_de_noticias_para_retorno):
    try:
        API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")
        client = OpenAI(api_key=API_KEY_OPENAI)

        schema = {
            "id1": "",
            "id2": "",
            "id3": "",
            "id4": "",
            "id5": "",
        }
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Responsável por ler o titulo e resumoNoticia do json recebido e retornar um json com as {qtd_de_noticias_para_retorno} melhores notícias, tendo em mente os interesses do mercado SMB no ramo da tecnologia."
                                              f"\nNão traga noticias sobre: 1 - celulares, 2 - cripto-moedas, 3 - jogos, 4 - hardware gamer"},
                {"role": "user", "content": f'Esqueça qualquer formatação json anterior. '
                                            f'\nEscolha as {qtd_de_noticias_para_retorno} melhores noticias do json a seguir: {noticias_json}\nUse o template a seguir para responder: {schema}'
                                            f'\nO schema deve seguir o padrão id1, id2... até o id{qtd_de_noticias_para_retorno}'}
                # {"role": "user", "content": f"Olá json!"}
            ],
            max_tokens=1500,
            response_format={"type": "json_object"},
            temperature=0.9
        )

        print("Retorno dentro da ia melhores noticias: ")
        print(completion.choices[0].message.content)
        dicionario_filtrado = completion.choices[0].message.content

        return dicionario_filtrado
    except Exception as e:
        print(e)
        return None


# print(filtro_html_para_json())