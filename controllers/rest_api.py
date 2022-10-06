import json
import requests

url = 'http://127.0.0.1:5000/'

resposta_hoteis = requests.request('GET', url + '/hoteis')

hoteis = resposta_hoteis.json()

# lista_hoteis = hoteis['hoteis']

print(hoteis)