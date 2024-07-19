import os

import requests
from openai import OpenAI
from repositorio.noticias_repositorio import adicionar_imagem


def get_request(url):
    image_response = requests.get(url)
    if image_response.status_code == 200:
        print("Request imagem OK!")
        return image_response
    else:
        print("Erro ao salvar imagem!")
        return None

def ia_fazer_imagem(titulo, resumo):
    try:
        API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")
        client = OpenAI(api_key=API_KEY_OPENAI)

        response = client.images.generate(
            model="dall-e-3",
            # prompt=f"Faça um gato olhando pela janela",
            prompt=f"Faça uma imagem com base nesse titulo: {titulo}\n e nesse texto: {resumo}.\n\nA imagem deve ter um contexto profissional e comercial no contexto.",
            n=1,
            size="1024x1024"
        )

        nome_arquivo = titulo + ".png"

        img_url = response.data[0].url
        print(img_url)
        response = get_request(img_url)
        if response is not None:
            try:
                id_imagem = adicionar_imagem(response, nome_arquivo)
                return id_imagem
            except Exception as e:
                print(e)
                return None
        else:
            return None

    except Exception as e:
        print(e)
        return None

# titulo = "Google prepara mega compra na área de segurança"
# resumo = "A Alphabet, holding controladora da Google, está em estágio avançado de negociações para adquirir a startup americana de cibersegurança Wiz por US$ 23 bilhões. Se concretizado, será a maior aquisição do grupo. O Wall Street Journal revelou as negociações, que ainda dependem de acordos sobre lucros para funcionários e de aprovações regulatórias, devido à fiscalização sobre a expansão de grandes empresas de tecnologia. A Google enfrenta desafios antitruste por seu domínio no mercado de pesquisa online e publicidade digital. Com o aumento da movimentação de startups para a nuvem, a segurança de dados sensíveis torna-se crucial. A Alphabet busca fortalecer seus negócios na nuvem com ferramentas de inteligência artificial generativa, aumentando a competição com a Microsoft, líder em produtos de segurança cibernética. Em 2022, a Alphabet adquiriu a Mandiant por US$ 5,4 bilhões. Fundada em Israel em 2020 e sediada em Nova York, a Wiz cresceu rapidamente, com 900 funcionários globalmente e planos de contratar mais 400 em 2024. Sua ferramenta de segurança baseada em nuvem detecta ameaças em tempo real e responde com inteligência artificial. Clientes incluem Morgan Stanley e DocuSign. Em 2023, a Wiz gerou US$ 350 milhões em receita e foi avaliada em US$ 12 bilhões após levantar US$ 1 bilhão em financiamento, atendendo 40% das empresas da Fortune 100."
# response = ia_fazer_imagem(titulo, resumo)
# print("Saída da função: \n" + response)
