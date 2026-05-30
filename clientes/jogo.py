import requests

# Colar a URL do Ngrok aqui, e dictionary /api.php no final

url_api = "https://enrage-cosigner-petite.ngrok-free.dev/meu-jogo/api.php"

print('Tentando conectar com o servidor...')

try:
    # O Python "bate" na porta da api
    response = requests.get(url_api)

##Transforma o JSON do PHP em um Dictionary do Python
    dados = response.json()

    print('\nConexão estabelecida!')
    print('Mensagem do servidor: ' + dados['mensagem'])

except Exception as erro:
    print('\nOps! não consegui conectar. O erro foi:')
    print(erro)
