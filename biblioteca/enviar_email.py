import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from biblioteca.data import converter_data_alema_para_br


API_GMAIL = os.getenv("API_KEY_GMAIL")

def enviar_email(noticias_json):
    # noticias_dicionario = json.loads(noticias_json)
    noticias_dicionario = noticias_json
    corpo_email = ""
    for i, noticia in enumerate(noticias_dicionario):
        data_br = converter_data_alema_para_br(noticia["data"])
        if i == 0:
            corpo_email = f"""
                <h3>Noticias {data_br}</h3>
                <br><br>
            """
        corpo_email += f"""
            <p>{noticia['fonte']} {data_br}</p>
            <h2>{noticia["titulo"]}</h2>
            <p>{noticia["resumoNoticia"]}</p>
            <u><a href={noticia['urlNoticia']}>Noticia completa</a></u>
        """
        if i < len(noticias_dicionario) - 1:
            corpo_email += "<hr>"

    # Configurações do email
    remetente = "viniciussilvano022@gmail.com"
    # destinatarios = ["viniciussilvano022@gmail.com", "vinicius@bestsoft.com.br"]
    destinatarios = ["viniciussilvano022@gmail.com", "vinicius@bestsoft.com.br", "julio@bestsoft.com.br", "rafaela@bestsoft.com.br"]
    senha = API_GMAIL

    # Criação da mensagem
    msg = MIMEMultipart()
    msg["From"] = remetente
    if len(destinatarios) > 1:
        msg["To"] = ', '.join(destinatarios)
    else:
        msg["To"] = destinatarios[0]
    msg["Subject"] = "Notícias do dia. TESTE"

    # Adicionando o corpo do email
    msg.attach(MIMEText(corpo_email, "html"))

    # Conectando ao servidor SMTP do Gmail
    try:
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(remetente, senha)
        s.sendmail(remetente, destinatarios, msg.as_string())
        s.quit()
        print("Email enviado com sucesso")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

# Chame a função para enviar o email
# enviar_email()
