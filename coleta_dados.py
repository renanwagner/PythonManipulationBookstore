import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

extracao = BeautifulSoup(requisicao.text, 'html.parser')

contar_livros = 0
catalogo = []
titulos = []
precos = []

for artigo in extracao.find_all('article', class_='product_pod'):
    livro = {}

    # Título
    h3 = artigo.find('h3')
    a_tag = h3.find('a')
    titulo = a_tag.text.strip()
    livro['Título'] = titulo
    titulos.append(titulo)

    # Preço
    preco_tag = artigo.find('p', class_='price_color')
    preco = preco_tag.text.strip()
    livro['Preço'] = preco
    precos.append(preco)

    catalogo.append(livro)
    contar_livros += 1

print(titulos)
print(precos)
print('contar_livros =', contar_livros)