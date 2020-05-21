import json
import string
import requests
import hashlib


def decrypt(cifrado, chave):
    mensagem = ''
    
    for contador in cifrado:
        try:
            i = (alfabeto.index(contador) - chave) % 26
            mensagem += alfabeto[i]
        except ValueError:
            mensagem += contador
    
    return mensagem

url_get = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token='
url_post = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token='

chave = 0
cifrado = ''
decifrado = ''
alfabeto = string.ascii_lowercase

requisicao = requests.get(url_get)

with open('answer.json', 'w') as arquivo:
    json.dump(requisicao.json(), arquivo)

with open('answer.json', 'r+') as arquivo:
    data = json.load(arquivo)
    cifrado = data['cifrado'].lower()
    chave = data['numero_casas']
    data['decifrado'] = decrypt(cifrado, chave)
    codificacao = arquivo.encoding
    data['resumo_criptografico'] = hashlib.sha1(data['decifrado'].encode(codificacao)).hexdigest()
    arquivo.seek(0)
    json.dump(data, arquivo)
    arquivo.truncate()

arquivo_final = {'answer': open('answer.json', 'rb')}
requisicao = requests.post(url_post, files=arquivo_final)
print(requisicao.json())
