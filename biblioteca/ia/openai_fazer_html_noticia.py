import json
import os

from openai import OpenAI
from biblioteca.extrair_json import extrair_json
from biblioteca.data import data_alema

# Essa função retorna um dicionario
def ia_fazer_html_noticia(html, prompt_extra = ""):
    try:
        API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")
        client = OpenAI(api_key=API_KEY_OPENAI)

        html_template = """
            <!DOCTYPE html>
            <html lang='en'>
            <head>
              <meta charset='UTF-8'>
              <meta name='viewport' content='width=device-width, initial-scale=1.0'>
              <style>
                body { font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0; }
                .email-container { max-width: 600px; margin: 20px auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
                .header { background-color: #4CAF50; padding: 10px; text-align: center; color: #ffffff; border-radius: 8px 8px 0 0; }
                .content { padding: 20px; }
                .footer { background-color: #f4f4f4; padding: 10px; text-align: center; color: #666666; font-size: 12px; border-radius: 0 0 8px 8px; }
                .button { display: inline-block; padding: 10px 20px; margin: 20px 0; color: #ffffff; background-color: #4CAF50; text-decoration: none; border-radius: 5px; }
              </style>
            </head>
            <body>
              <div class='email-container'>
                <div class='header'>
                  <h1>{titulo}</h1>
                </div>
                <div class='content'>
                  <p><strong>Fonte:</strong> {fonte}</p>
                  <p><strong>Data:</strong> {data}</p>
                  <p><strong>Resumo:</strong> {resumo}</p>
                  <p><a href='{urlNoticia}' class='button'>Leia a notícia completa</a></p>
                </div>
                <div class='footer'>
                  <p>&copy; 2024 Seu Nome ou Empresa. Todos os direitos reservados.</p>
                </div>
              </div>
            </body>
            </html>
        """

        schema = {
          "html": "",
        }

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Responsável por ler a noticia recebida e formular um arquivo html no seguinte formato ({html_template}). A respostá será um html dentro do json no seguinte formato: {schema}"},
                {"role": "user", "content": f"Responsável por ler a noticia recebida e formular um arquivo html no seguinte formato ({html_template}). A respostá será um html dentro do json no seguinte formato: {schema}"}
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