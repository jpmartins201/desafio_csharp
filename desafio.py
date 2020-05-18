import json
import string
import requests
import hashlib

url_get = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token='
url_post = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token='

chave = 0
cifrado = ''
decifrado = ''
alfabeto = string.ascii_lowercase

requisicao = requests.get(url_get)

with open('answer.json', 'w') as arquivo:
    json.dump(requisicao.json(), arquivo)
