import pandas as pd

#Series e Dataframe: a estrutura geral do Pandas.
#Estudo de análise, organização de dados e estrutura de um dataframe.


ex_dict = {'Times': ['Brasil', 'Uruguai', 'Alemanha', 'Argentina', 'Italia', 'EUA'], 'Vitorias': [9, 6, 6, 7, 4, 5], 'Derrotas': [1, 1, 2, 3, 1, 4]}

print(ex_dict)

#É possivel gerar um dataframe a partir de dicionarios 
#Note o pd de pandas

df = pd.DataFrame.from_dict(ex_dict)
print(df)

       Times  Vitorias  Derrotas
0     Brasil         9         1
1    Uruguai         6         1
2   Alemanha         6         2
3  Argentina         7         3
4     Italia         4         1
5        EUA         5         4

#Note a cima a estrutura dos dados no dicionário e depois no dataframe após o print.
#Temos cada coluna, contendo as linhas com as informações.

#SERIES: é um conjunto unidimensional contendo dados em diversas formas (int,float,objetos,etc.).É bastante similar ao numpy.array, coluna única.

#Dataframe: É um conjunto bidimensional de dados.Pode ser entendido como um conjunto de Series.



#Series pode ser gerado a partir do comando pandas.Series()
#Note a numeração das linhas e compare com a estrutura de um array de numpy, por exemplo

series = pd.Series(ex_dict['Vitorias'])
print(series)
0    9
2    6
3    7
4    4
5    5

#ENTENDENDO A ESTRUTURA E ORGANIZAÇÃO DOS DADOS: OPÇÕES BÁSICAS:

#Para Importar arquivo
#Lembrando que o csv é um arquivo "comma-separated" comum em programas de planilha tipo excel.

#use o codigo de comando abaixo
df = pd.read_csv('ex_pandas_csv.csv', sep=';')


#primeiro, vamos ter uma ideia geral dos dados...
#O comando dataFrame.shape retorna o número de linhas e colunas

print(df.shape)
(6, 3)


#O comando DataFrame.head()  imprime as linhas iniciais do dataframe

print(df.head())

       Times  Vitorias  Derrotas
0     Brasil         9         1
1    Uruguai         6         1
2   Alemanha         6         2
3  Argentina         7         3
4     Italia         4         1
5        EUA         5         4


#E dos dados finais...
#O comando DataFrame.tail()  imprime as linhas finais do dataframe

print(df.tail(2))

4  Italia         4         1
5     EUA         5         4


#Vendo quais colunas existem no dataset todo

print(df.columns)
Index(['Times', 'Vitorias', 'Derrotas'], dtype='object')


#O comando DataFrame.describe()  traz informações de cada coluna

print(df.describe())
       Vitorias  Derrotas
count  6.000000  6.000000
mean   6.166667  2.000000
std    1.722401  1.264911
min    4.000000  1.000000
25%    5.250000  1.000000
50%    6.000000  1.500000
75%    6.750000  2.750000
max    9.000000  4.000000


#O DataFrame.sum()  Tras a soma dos dados
#Lembre que, no python a operação de soma (+) de string concatena as palavras

print(df.sum())
Times       BrasilUruguaiAlemanhaArgentinaItaliaEUA
Vitorias                                         37
Derrotas                                         12
dtype: object



