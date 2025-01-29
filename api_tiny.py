import requests
import json
import time

def pesquisar_produtos(TOKEN_TINY, url_params):
    url = f'https://api.tiny.com.br/api2/produtos.pesquisa.php?token={TOKEN_TINY}&formato=json' + ''.join([f'&{k}={v}' for k, v in url_params.items()])
    print(url)

    payload = ''
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response

def alterar_produto(TOKEN_TINY, id_pedido, pedido):
    url = f'https://api.tiny.com.br/api2/pedido.alterar.php?token={TOKEN_TINY}&formato=json&id={id_pedido}'
    print(url)

    payload = json.dumps(pedido)
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()
