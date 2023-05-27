from key import API_KEY
import requests
import json
import smtplib
import email.message

# 1. INTEGRAÇÃO CHATGPT COM PYTHON - REST API OPENAI #

# DICIONÁRIO DE HEADERS #
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

# LINKS #
modelsLink = "https://api.openai.com/v1/models"
chatLink = "https://api.openai.com/v1/chat/completions"

# ID DO CHATGPT TURBO 3.5 #
idGptTurbo = "gpt-3.5-turbo"

requisicaoGet = requests.get(modelsLink, headers=headers)

""" testando requisição
print(requisicao)
print(requisicao.text)
"""

# TRABALHANDO COM O CHAT #
body_msg = {
    "model": idGptTurbo,
    "messages": [{ "role": "user" , "content": "Me indique uma receita saudável, barata e sustentável"}]
}

# TRANSFORMANDO EM JSON #
body_msg = json.dumps(body_msg)

requisicaoPost = requests.post(chatLink, headers=headers, data=body_msg)
print(requisicaoPost)
print(requisicaoPost.text)

# TRANSFORMANDO JSON EM DICIONÁRIO PYTHON PARA TRATAR #
response = requisicaoPost.json()
response_msg = response["choices"][0]["message"]["content"]
print(response_msg)


# 2. ENVIO DE E-MAIL AUTOMÁTICO #

def enviar_email():
    body_email = response_msg

    msg = email.message.Message()
    msg['Subject'] = "Resposta para a sua pergunta via Plataforma:"
    # Substituir pelo e-mail da empresa #
    msg['From'] = "andre.melo9715@gmail.com"
    # Substituir pelo e-mail do usuário #
    msg['To'] = "andre.melo9715@gmail.com"
    password = 'senha'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body_email)

    s = smtplib.SMTP('smtp.gmail.com: 587') ## SMTP padrão GMAIL
    s.starttls()
    # Credenciais #
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))

    """ TESTE ENVIO
    print('Email enviado com sucesso!')
    """