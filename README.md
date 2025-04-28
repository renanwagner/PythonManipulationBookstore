# What is 'PythonManipulationBookstore'?
A data manipulation project of a bookstore in python(PyCharm)

* How 'coleta_dados' it works?
- The file introduce the data select and collection from web, using requests, BeautifoulSoup and pandas. The functions are:
    - 'extracao', extract data from the website, reading html.
    - 'titulos.append', count the titles in the text, classified by 'h3'.
    - 'precos.append', count the prices in the text, defined by 'price_color', transform in strip and associate with livro['Preço']
    - 'catalogo.append' and 'contar_livros +=1' count the amount of books in the store, adding 1 every time that a diferent product is identified.
  - Finish with a print of all functions results.
