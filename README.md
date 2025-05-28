📘 PythonManipulationBookstore
## A data manipulation project for a bookstore, developed in Python using PyCharm.
This project is divided into two main parts:

## Data Collection (coleta_dados.py)

## Data Cleaning and Transformation (tratamento_dados.py)

# 📚 Web Scraping and Book Data Processing

This project collects and processes book data from an online store using Python libraries such as `requests`, `BeautifulSoup`, and `pandas`.

---

## 📦 Module 1: Data Extraction (`extracao.py`)

This script handles the extraction of data directly from the website, organizing and storing key book information.

### 🔧 Main Functions

- **`extracao`**  
  Extracts data from the web page using `requests` and `BeautifulSoup`.

- **`titulos.append()`**  
  Collects all book titles found in specific HTML tags.

- **`precos.append()`**  
  Captures all prices found under the `price_color` class, cleans them using `.strip()`, and stores them in the `livro['Preço']` field.

- **`catalogo.append()` & `contar_livros += 1`**  
  Appends each identified book to the catalog and increments the total count of books.

### ✅ Final Output

At the end of execution, the script prints all collected titles, prices, and the total number of books found.

---

## 🧹 Module 2: Data Cleaning and Analysis (`tratamento_dados.py`)

This script performs data cleaning, transformation, and basic exploratory analysis using `pandas`.

### 🔄 Step-by-Step Process

#### 📂 1. Load the Dataset

Load the CSV file into a pandas DataFrame:

```python
pd.read_csv('your_file.csv')
🧪 2. Inspect Data Structure and Quality
Check number of rows and columns:

python
Copiar
Editar
df.shape
Check data types:

python
Copiar
Editar
df.dtypes
Count missing values:

python
Copiar
Editar
df.isnull().sum()
🧼 3. Handle Missing Data
Replace missing values in Temporada and Marca:

python
Copiar
Editar
df['Temporada'].fillna('Not Defined', inplace=True)
df['Marca'].fillna('Not Defined', inplace=True)
🔠 4. Standardize Text Columns
Convert to lowercase:

python
Copiar
Editar
df['Marca'] = df['Marca'].str.lower()
df['Material'] = df['Material'].str.lower()
df['Temporada'] = df['Temporada'].str.lower()
🧹 5. Remove Redundant or Incomplete Data
Remove duplicates:

python
Copiar
Editar
df.drop_duplicates(inplace=True)
Drop rows with fewer than 8 non-null values:

python
Copiar
Editar
df.dropna(thresh=8, inplace=True)
🚨 6. Detect and Isolate Outliers
Identify outliers in the N_Avaliacoes column:

python
Copiar
Editar
Q1 = df['N_Avaliacoes'].quantile(0.25)
Q3 = df['N_Avaliacoes'].quantile(0.75)
IQR = Q3 - Q1
upper_threshold = Q3 + 1.5 * IQR
outliers = df[df['N_Avaliacoes'] > upper_threshold]
🧩 7. Parse and Transform Complex Columns
Extract condition status and quantity sold:

python
Copiar
Editar
df['Condicao_Atual'] = df['Condicao'].str.split('|').str[0]
df['Qtd_Vendidos'] = df['Condicao'].str.split('|').str[1].fillna('None')
Clean discount column:

python
Copiar
Editar
df['Desconto'] = df['Desconto'].astype(str).apply(lambda x: x.replace('%', ''))
📌 Technologies Used
Python 3.x

pandas

requests

BeautifulSoup
