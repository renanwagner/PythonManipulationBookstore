📘 PythonManipulationBookstore
## A data manipulation project for a bookstore, developed in Python using PyCharm.
This project is divided into two main parts:

## Data Collection (coleta_dados.py)

## Data Cleaning and Transformation (tratamento_dados.py)

# 📥 How coleta_dados.py Works
###] This script handles the selection and collection of book data from the web, using the libraries requests, BeautifulSoup, and pandas.

##🔧 Main Functions
extracao
Extract data from the website by reading the HTML content.

titulos.append
Collect all book titles found in <h3> tags.

precos.append
Capture all prices identified by the 'price_color' class, clean them using .strip(), and associate each value with livro['Preço'].

catalogo.append & contar_livros += 1
Count and store each unique book found in the store, incrementing the counter for every identified product.

✅ Finish by printing the results of all these operations.

🧹 How tratamento_dados.py Works
This script performs data cleaning, transformation, and basic exploratory analysis using pandas.

🔄 Step-by-step Process
📂 Load the Dataset
Load the CSV file into a pandas DataFrame using:

python
Copiar
Editar
pd.read_csv()
🧪 Check Structure and Quality
Check the number of rows and columns using .shape.

Check the data types of each column with .dtypes.

Count missing values in each column using .isnull().sum().

🧼 Handle Missing Data
Replace missing values in the 'Temporada' and 'Marca' columns with 'Não Definido' using:

python
Copiar
Editar
.fillna()
🔠 Standardize Text Columns
Convert the following columns to lowercase using .str.lower():

'Marca'

'Material'

'Temporada'

🧹 Remove Redundant or Incomplete Data
Remove duplicate rows using:

python
Copiar
Editar
.drop_duplicates()
Remove rows with fewer than 8 non-null values using:

python
Copiar
Editar
.dropna(thresh=8)
🚨 Detect and Isolate Outliers
Calculate the Interquartile Range (IQR) for the 'N_Avaliacoes' column.

Define an upper threshold as:

python
Copiar
Editar
Q3 + 1.5 * IQR
Filter products that exceed this threshold to identify outliers or highly-reviewed items.

🧩 Parse and Transform Complex Columns
Extract the first segment (before '|') from the 'Condicao' column and store it in 'Condicao_Atual'.

Extract the quantity of units sold from the second segment of 'Condicao', or return 'Nenhum' if unavailable. Store the result in 'Qtd_Vendidos'.

Convert the 'Desconto' column to string format and remove the % symbol using a lambda function.

📌 Technologies Used
Python 3.x

pandas

requests

BeautifulSoup
