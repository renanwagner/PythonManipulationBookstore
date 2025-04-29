# What is 'PythonManipulationBookstore'?
A data manipulation project of a bookstore in python(PyCharm)

* How 'coleta_dados' works:
-- The file introduce the data select and collection from web, using requests, BeautifoulSoup and pandas. The functions are:
-- 'extracao', extract data from the website, reading html.
-- 'titulos.append', count the titles in the text, classified by 'h3'.
-- 'precos.append', count the prices in the text, defined by 'price_color', transform in strip and associate with livro['Preço']
-- 'catalogo.append' and 'contar_livros +=1' count the amount of books in the store, adding 1 every time that a diferent product is identified.
-- Finish with a print of all functions results.

* How 'tratamento_dados' works:
** This script handles the cleaning, transformation, and exploratory steps for datasets from an e-commerce platform using pandas.

* Step-by-step Process
-- Load the dataset
-- Read the CSV file into a pandas DataFrame using pd.read_csv().
-- Check structure and quality
-- Use .shape to inspect the number of rows and columns.
-- Use .dtypes to check data types of each column.
-- Use .isnull().sum() to count missing values per column.
-- Handle missing data
-- Replace null values in the 'Temporada' and 'Marca' columns with 'Não Definido' using .fillna().
-- Standardize text columns
-- Convert 'Marca', 'Material', and 'Temporada' columns to lowercase using .str.lower().
-- Remove redundant or incomplete data
-- Remove duplicate rows using .drop_duplicates().
-- Remove rows with fewer than 8 non-null values using .dropna(thresh=8).
-- Detect and isolate outliers
-- Calculate the interquartile range (IQR) of the 'N_Avaliacoes' column.
-- Define an upper threshold using Q3 + 1.5 * IQR.
-- Filter products with review counts above this threshold to identify popular or anomalous items.
-- Parse and transform complex string columns
-- Extract the first segment of the 'Condicao' column (before the pipe symbol |) and store it in 'Condicao_Atual'.
-- Extract the quantity of units sold from the second segment of 'Condicao' if available; otherwise, return 'Nenhum', and store it in 'Qtd_Vendidos'.
- Convert the 'Desconto' column to string format and remove the % symbol using a lambda function.
