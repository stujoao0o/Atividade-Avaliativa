import requests
from bs4 import BeautifulSoup

# URL da página que contém os nomes dos professores
url = 'https://tribunademinas.com.br/noticias/cultura'

# Se conecta ao site do campus
response = requests.get(url)

# Verifica se a conexão foi bem-sucedida
if response.status_code == 200:
    html_content = response.text
    
    soup = BeautifulSoup(html_content, 'html.parser')

    #lista_manchetes = []
    all_div = soup.find_all('div', class_='col-sm-12')

    for div in all_div:
        all_h2 = div.find_all('h2')
        for h2 in all_h2:
            print(h2.text)
