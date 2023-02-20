import requests, sys
from termcolor import colored
#programa para verificar se o parametro reflete na página

try:
    arquivo = input(colored('Arquivo >>> ', 'green'))
    with open(arquivo, 'r') as arqv:
        for lista in arqv.read().split('\n'):
            try:
                if '<content>' in requests.get(lista).text:
                    print(colored(f'{lista}', 'green'))
                    with open('rpv_response.txt', 'a') as rpv:
                        rpv.write(f'\n{lista}')
                else:
                    print(colored(f'{lista}', 'red'))
            except KeyboardInterrupt:
                print(colored('--- CLOSED ---', 'red'))
                sys.exit(0)
except (FileNotFoundError, KeyboardInterrupt):
    print('\n')
    sys.exit(0)
        
    
