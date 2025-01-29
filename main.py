import os
import time
from dotenv import load_dotenv
import pandas as pd
from api_tiny import pesquisar_produtos
from api_miliapp import obter_item_miliapp

load_dotenv()
TOKEN_TINY = os.getenv('TOKEN_TINY')
TOKEN_MILIAPP = os.getenv('TOKEN_MILIAPP')

def main():
    os.system('cls')
    pagina = 1
    total_paginas = 2
    lista_produtos = []
    lista_atualizacao = []

    while pagina <= total_paginas:
        try:
            print(f'Página {pagina}')
            url_params = {
                'pagina': pagina,
                'situacao': 'A' 
            }

            response = pesquisar_produtos(TOKEN_TINY, url_params)
            time.sleep(1)
            response_json = response.json()
            status = response_json['retorno']['status']

            if status == 'OK':
                total_paginas = response_json['retorno']['numero_paginas']
                print(f'Total de páginas: {total_paginas}')
                response_lista_produtos = response_json['retorno']['produtos']

                for produto in response_lista_produtos:
                    lista_produtos.append(produto['produto'])
                pagina += 1
        except Exception as e:
            print(f'Erro: {e}')

    print(f'Total de produtos: {len(lista_produtos)}')
    salvar_produtos_em_planilha(lista_produtos, 'produtos_tiny_api.xlsx')

    for produto in lista_produtos:
        id_produto = produto['id']
        nome = produto['nome']
        print(nome)
        codigo = produto['codigo']

        url_params = {
            'token': TOKEN_MILIAPP,
            'idTiny': id_produto
        }

        response = obter_item_miliapp(url_params)
        time.sleep(1)
        print(response)
        if response['metadata']['count'] > 0:
            if nome != response['data'][0]['nome']:
                produto['novo_nome'] = response['data'][0]['nome']
                lista_atualizacao.append(produto)
            else:
                continue
        else:
            continue
    salvar_produtos_em_planilha(lista_atualizacao, 'produtos_atualizado.xlsx')
    
def salvar_produtos_em_planilha(lista_produtos, nome_arquivo='produtos.xlsx'):
    df = pd.DataFrame(lista_produtos)
    df.to_excel(nome_arquivo, index=False)
    print(f'Planilha salva como {nome_arquivo}')
    return


main()

            
