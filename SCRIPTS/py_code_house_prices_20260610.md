# House Prices - Kaggle


{python}
# Carregando as bibliotecas ...
import numpy as np
import pandas as pd
from IPython.display import display

# Carregando o dataset ...
dados_train=pd.read_csv("/home/delfos/Documentos/UEPB_20260326/PEDRO_MONTEIRO/CONSULTANCY/CONSULTANCY_PROJECTS/HOUSE_PRICES_PROJECT/DATA/house-prices-advanced-regression-techniques/train.csv")

# Zoiando
dados_train.head()  #5 primeiras linhas

# Para vê os tipos de dados e se há valores nulos
dados_train.info()

# Mudando a config p/exibir TODAS as linhas da tabela/série. O pandas esconde com "..."
pd.set_option("display.max_rows",None)

# Contando quantos NAs
dados_train.isnull().sum().sort_values(ascending=False)
#.isnull(): Identifica o que é nulo.
#.sum(): Soma os valorees or coluna.
#sort_values(ascending=False): Ordena os valores do maior para o menor.

# Porcentagem dos NAs
(dados_train.isnull().sum() / len(dados_train) * 100).sort_values(ascending=False)



{python}
# Para não bagunçar o Dataset original
dados_copia=dados_train.copy()

# Identificar col qualitativas (object e category)
qualitativas=dados_copia.select_dtypes(include=["object","category","string"]).columns

# Identificar col quantitativas (int,float)
quantitativas=dados_copia.select_dtypes(include=["int64","float64"]).columns

# Preencher "None" nas colunas qualitativas com NAs
dados_copia[qualitativas]=dados_copia[qualitativas].fillna("None")

# Preenche "0" nas colunas quantitativas com NAs
dados_copia[quantitativas]=dados_copia[quantitativas].fillna(0)

exit



{r}
#Não há um view que preste em Python! Logo,...
library(dplyr)

# Puxa os dados do Python como se fosse R
dados_r<-py$dados_copia

# Verificando a tabela
View(dados_r)



{python}
# Selencionando algumas variáveis para análise descritiva inicial

variaveis_primeira_analise=["SalePrice","LotArea","GarageCars","BedroomAbvGr"]

# Criando um dicionário para armazenar as estatísticas

estatisticas={
  "Média":dados_train[variaveis_primeira_analise].mean(),
  "Mediana":dados_train[variaveis_primeira_analise].median(),
  "Desvio Padrão":dados_train[variaveis_primeira_analise].std()
}

# Criando o DataFrame
tabela_descritiva=pd.DataFrame(estatisticas)
print(tabela_descritiva)

# Calculando o coeficiente de variação
# CV%=(dp/média)*100
# Criando nova coluna
tabela_descritiva["CV(%)"]=(tabela_descritiva["Desvio Padrão"]/tabela_descritiva["Média"])*100

# Arredondando p/2 casa decimais
tabela_descritiva=tabela_descritiva.round(2)
print(tabela_descritiva)



{python}
import seaborn as sns
import matplotlib.pyplot as plt

# Configurando o estilo dos gráficos
sns.set_theme(style="whitegrid")
#whitegrid: Fundo br c/line de grades

# Colocar os 3 graphics lado a lado
#fig,axes=plt.subplots(1,3,figsize=(18,5))
#plt.subplots: Vários graphics em uma mesma img.
#plt.subplots(line,col,tamanhoDaFigura=(largura,altura))
#fig:Retorne figura
#axes: array c/3 subplots

# Criando o Histograma
plt.figure(figsize=(8, 5)) # Define o tamanho desta janela específica
sns.histplot(dados_train['SalePrice'], kde=False, color='skyblue')
plt.title('Histograma de SalePrice')
plt.xlabel('Preço de Venda ($)')
plt.ylabel('Frequência')
plt.show() # Fecha a janela atual e exibe o gráfico

# Densidade
plt.figure(figsize=(8, 5)) 
sns.kdeplot(dados_train['SalePrice'], fill=True, color='purple')
plt.title('Gráfico de Densidade de SalePrice')
plt.xlabel('Preço de Venda ($)')
plt.ylabel('Densidade')
plt.tight_layout()
plt.show()

# Boxplot
plt.figure(figsize=(6, 5)) # Um pouco mais estreito porque boxplot vertical fica melhor assim
sns.boxplot(y=dados_train['SalePrice'], color='lightgreen')
plt.title('Boxplot de SalePrice')
plt.ylabel('Preço de Venda ($)')
plt.show()
