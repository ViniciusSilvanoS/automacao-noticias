import os

from openai import OpenAI


def imagem_profissional_noticia (titulo, resumo):
    try:
        API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")
        client = OpenAI(api_key=API_KEY_OPENAI)

        nome = titulo + '.png'

        response = client.images.generate(
            model="dall-e-3",
            # prompt=f"Faça um gato olhando pela janela",
            prompt=f"Faça uma imagem com base nesse titulo: {titulo}\n e nesse texto: {resumo}.\n\nA imagem deve ter um contexto profissional e comercial no contexto.",
            n=1,
            size="1024x1024"
        )

        img_url = response.data[0].url
        return img_url
    except Exception as e:
        print(e)
        return None