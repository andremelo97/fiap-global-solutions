from key import API_KEY
import requests
import json

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