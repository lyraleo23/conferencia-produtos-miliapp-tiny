import requests
import json

def obter_item_miliapp(url_params):
    url = f'https://api.fmiligrama.com/produtos/busca?' + ''.join([f'&{k}={v}' for k, v in url_params.items()])

    payload = {}
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()
