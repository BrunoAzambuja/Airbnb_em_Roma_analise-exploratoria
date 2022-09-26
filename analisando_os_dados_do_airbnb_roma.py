# -*- coding: utf-8 -*-
"""Analisando_os_Dados_do_Airbnb_Roma.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qr33QU4xJ_nbGvVdANKLXWwsJC1fvj1O

# Análise dos dados do Airbnb - Roma
*by [Bruno Azambuja](www.brunoazambuja.com)*

<center><img alt="Analisando Airbnb" width="30%" src="https://www.area360.com.au/wp-content/uploads/2017/09/airbnb-logo.jpg"></center>

O [Airbnb](https://www.airbnb.com.br/) já é considerado como sendo a **maior empresa hoteleira da atualidade**. Ah, o detalhe é que ele **não possui nenhum hotel**!

Conectando pessoas que querem viajar (e se hospedar) com anfitriões que querem alugar seus imóveis de maneira prática, o Airbnb fornece uma plataforma inovadora para tornar essa hospedagem alternativa.

No final de 2019, a Startup fundada 10 anos atrás, já havia **hospedado mais de 500 milhões** de pessoas ao redor de todo o mundo, desafiando as redes hoteleiras tradicionais.

Uma das iniciativas do Airbnb é disponibilizar dados do site, para algumas das principais cidades do mundo. Por meio do portal [Inside Airbnb](http://insideairbnb.com/get-the-data.html), é possível baixar uma grande quantidade de dados para desenvolver projetos e soluções de *Data Science*.

## Roma, capital da Itália

<center><img alt="Roma" width="75%" src="https://astelus.com/wp-content/viajes/Que-ver-en-Roma-1152x759.jpg"></center>

Dentre os dados de algumas das principais cidades disponibilizados pelo Inside Airbnb, Roma foi a cidade escolhida para o desenvolvimento deste projeto, que está entre os locais que mais se atrai visitantes no mundo.

Roma, a capital da Itália, é uma cidade cosmopolita, enorme, com quase 3.000 anos de arte, arquitetura e cultura influentes no mundo todo, nela se encontra obras de arte entre a arquitetura de suas belas ruas, como a Fontana di Trevi, demonstrando ao mundo porque Roma é considerada o **"berço da cultura e da civilização ocidental"**.

Ruínas antigas como o Fórum, o Panteão e o Coliseu evocam o poder do antigo Império Romano. A Cidade do Vaticano, sede da Igreja Católica Romana, tem a Basílica de São Pedro e os museus do Vaticano, que abrigam obras-primas como os afrescos da Capela Sistina de Michelângelo.

<center><img alt="Vatican" width="75%" src="https://i0.wp.com/travelbluebook.com/wp-content/uploads/2015/11/Pantheon-at-Night.jpg?w=1200&ssl=1"></center>

A história de Roma abrange 28 séculos, apesar da mitologia romana data a fundação de Roma por volta de 753 a.C., o local é habitado há muito mais tempo, tornando-se um importante assentamento humano por quase três milênios e uma das mais antigas cidades continuamente ocupadas da Europa.

Eventualmente, a cidade tornou-se sucessivamente a capital do Reino Romano, da República Romana e do Império Romano, sendo considerada por muitos como a primeira cidade e metrópole imperial.

Em 2019, Roma foi a 11ª cidade mais visitada do mundo, com 10,1 milhões de turistas, a **terceira mais visitada na União Europeia** e o destino turístico mais popular da Itália. O seu centro histórico está classificado pela UNESCO como um **Patrimônio Mundial**.

Roma é a sede de várias agências especializadas das Nações Unidas, como a Organização das Nações Unidas para a Alimentação e a Agricultura (FAO), o Programa Alimentar Mundial (PAM) e o Fundo Internacional de Desenvolvimento Agrícola (FIDA), além da presença de renomadas marcas internacionais na cidade, que fez de Roma também um **importante centro de moda e design**, e os estúdios Cinecittà foram cenário de muitos filmes vencedores do Oscar.

Fonte: [wikipedia](https://pt.wikipedia.org/wiki/Roma)

## Premissas estabelecidas para o projeto

Neste *notebook*, iremos analisar os dados referentes à cidade de Roma, e ver quais insights podem ser extraídos a partir de dados brutos.

## Obtenção dos dados

Todos os dados utilizados aqui foram obtidos a partir do portal [Inside Airbnb](http://insideairbnb.com/get-the-data).

Para esta análise exploratória inicial, será baixado apenas o seguinte arquivo :

'listings.csv' - Summary information and metrics for listings in Rome (good for visualisations).
"""

# Commented out IPython magic to ensure Python compatibility.
# importar os pacotes necessarios
import folium
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib
import matplotlib.image as mpimg
from folium.plugins import HeatMap
from folium.plugins import FastMarkerCluster
# %pip install branca==0.3.1

# importar o arquivo listings.csv para um DataFrame
df = pd.read_csv("http://data.insideairbnb.com/italy/lazio/rome/2022-06-07/visualisations/listings.csv")

"""## Análise dos dados
Esta etapa tem por objetivo criar uma consciência inicial e permitir um entendimento de como os dados estão estruturados

**Dicionário das variáveis**

* `id` - número de id gerado para identificar o imóvel
* `name` - nome da propriedade anunciada
* `host_id` - número de id do proprietário (anfitrião) da propriedade
* `host_name` - Nome do anfitrião
* `neighbourhood_group` - esta coluna não contém nenhum valor válido
* `neighbourhood` - nome do bairro
* `latitude` - coordenada da latitude da propriedade
* `longitude` - coordenada da longitude da propriedade
* `room_type` - informa o tipo de quarto que é oferecido
* `price` - preço para alugar o imóvel
* `minimum_nights` - quantidade mínima de noites para reservar
* `number_of_reviews` - número de reviews que a propriedade possui
* `last_review` - data do último review
* `reviews_per_month` - quantidade de reviews por mês
* `calculated_host_listings_count` - quantidade de imóveis do mesmo anfitrião
* `availability_365` - número de dias de disponibilidade dentro de 365 dias

Antes de iniciar qualquer análise, vamos verificar a cara do nosso *dataset*, analisando as 5 primeiras entradas.
"""

# mostrando as 5 primeiras entradas
df.head()

"""### **Identificando a quantidade de atributos (variáveis) e entradas o nosso conjunto de dados possui, assim como quais os tipos das variáveis**"""

# identificando o volume de dados do DataFrame
print("Entradas/Linhas do dataset:\t {}".format(df.shape[0]))
print("Variáveis/Colunas do dataset:\t {}\n".format(df.shape[1]))

# verificando as entradas do dataset
display(df.dtypes)

"""### **Verificando e removendo valores ausentes no dataset**

**Tratando os Dados ausentes**

Ao iniciar a análise dos dados ausentes alguns pontos foram considerados como: 

Que tipo de dado está ausente? Em qual proporção? De forma aleatória? 

Todos esses são aspectos que foram levados em consideração ao tratar os dados ausentes. Especialmente em algumas variáveis onde o volume é muito grande e qualquer tipo de preenchimento poderia enviesar os dados de forma que a análise deixasse de ser relevante.

Para outros casos, foram considerados as seguintes hipóteses:

* Excluir
  * Se os dados ausentes estão em pequeno número, ocorrem aleatoriamente, e a ausência não carrega significado, é melhor excluir a linha. No caso da coluna, se ainda for possível analisar alguma parte dela, use-a, como é o caso aqui. Mas para algumas situações, o ideal é excluir a coluna.

* Preencher
  * Preencher as entradas com dados ausentes com valores estatísticos como a média, mediana, moda ou zeros.
  * A média é mais útil quando a distribuição dos dados é normal. Em dados com distribuição mais enviesada (*skewed*), a mediana é uma solução mais robusta, pois ela é menos sensível a outliers.
  * Uma `Regressão Linear` também pode ser útil, apesar de sensível a outliers, podem nos ajudar a inserir valores que nos ajudem.
  * Indentificar a entrada ausente com algum valor que indique isso pode ser mais informativo, quando a ausência representa valor. Por exemplo, em dados numéricos preencher com zero, e em categóricos criar uma categoria "Desconhecido". Atenção, pois os zeros não podem ser levados em consideração em análises estatísticas.
"""

# ordenando em ordem decrescente as variáveis por seus valores ausentes
(df.isnull().sum() / df.shape[0]).sort_values(ascending=False)

"""Considerando os pontos levantados como estratégia de tratamento dos dados ausentes, assim como os dados levantados da quantidade de valores ausentes neste dataset e as suas respectivas relevâncias para os objetivos propostos neste projeto, optou-se pela exclusão das colunas `neighbourhood_group`, `last_reviews` e `license`.

Para a coluna `reviews_per_month` foi realizado o preenchimento dos valores ausentes pela mediana da sua respectiva coluna.

Já para os valores ausentes do `host_name`e `name` optou-se pela exclusão destas linhas.
"""

# convertendo os tipos de dados das colunas
df[['price','latitude', 'longitude','reviews_per_month']] = df[['price','latitude', 'longitude', 'reviews_per_month']].astype('float')

# excluindo as colunas com os dados faltantes e não relevante
df.drop(columns=['neighbourhood_group', 'license', 'last_review'], inplace=True)

# preenchendo os valores ausentes da coluna com a mediana
rpm_median = df.reviews_per_month.median()
df.fillna({"reviews_per_month": rpm_median}, inplace=True)

# excluindo as entradas com dados faltantes
df.dropna(axis=0, inplace=True)

"""Verificando o tratamento dos valores ausentes do dataset"""

# ordenando em ordem decrescente as variáveis por seus valores ausentes
(df.isnull().sum() / df.shape[0]).sort_values(ascending=False)

# identificando o volume de dados do DataFrame
print("Entradas/Linhas:\t {}".format(df.shape[0]))
print("Variáveis/Colunas:\t {}\n".format(df.shape[1]))

"""Como pode ser visto todos os valores ausentes foram removidos do dataset, preservando de forma significativa o montante de dados disponibilizados inicialmente.

Desta forma o tratamento dos dados ausentes alcançou o objetivo proposto, preservando os dados para que se possa tirar os insights desejados neste projeto.

### **Identificando e retirando outliers presentes no dataset?**

*Outliers* são pontos discrepantes, que estão destoando do padrão do conjunto de dados.

É muito importante conseguir identificar e tratar esses outliers, pois eles podem nos mostrar uma imagem incorreta dos nossos dados.

Podemos identificar um outlier de diversas formas, entre elas podemos citar:

* IQR Score
* Boxplots
* Scatter plots
* Z-Score

Para tratar dos outliers desse conjunto de dados, iremos analisar a distribuição estatística, plotar boxplots e calcular os limites utilizando a regra do IQR Score.

Primeiramente, vamos lembrar o que é o IQR.

O IQR é calculado subtraindo o Terceiro Quartil (75%) pelo Primeiro Quartil (25%).

IQR = Q3 - Q1
Vamos dar uma olhada nos nossos dados e ver o que identificamos.
"""

# verificando a distribuição estatística
df.describe().round(1)

"""Aqui, algumas coisas já chamam a nossa atenção, como por exemplo:

* A variável `price` tem o mínimo em 0.
* Lembrando que a variável `price` trata do preço da diária dos imóveis em moeda local (USD), estamos vendo que o Q3 está em 157 dólares, mas o máximo está em 90 mil dólares. Claramente, há outliers por aqui.
* A variável `minimum_nights` tem como seu máximo o valor 1000, sendo que o Q3 está em 3. Claramente temos outliers nessa variável.
* As variáveis `number_of_reviews`, `reviews_per_month` e `calculated_host_listings_count` também podem conter outliers, mas não vamos nos preocupar com elas agora.
"""

# verificando as distribuições
df.hist(figsize=(15,10), grid=False);

"""Verificando os histogramas, conseguimos ver claramente que temos outliers presentes. Para tratá-los vamos seguir os seguintes passos:

* Definir o Q1 e Q3 para as variáveis que serão limpas;
* Calcular o IQR para as variáveis;
* Definir o limite superior e inferior para cortar os outliers;
* Remover os outliers;
* Visualizar e analisar novamente os dados tratados.

**Definindo o Q1 e Q3 para as variáveis que serão limpas, calculando o IQR para as variáveis e definindo o limite superior e inferior para cortar os outliers das variáveis `price` e `minimum_nights`**
"""

# identificando os outliers para a variável Price
q1_price = df.price.quantile(.25)
q3_price = df.price.quantile(.75)
IQR_price = q3_price - q1_price
print('IQR da variável price: ', IQR_price)

# definindo os limites para a variável Price            
sup_price = q3_price + 1.5 * IQR_price
inf_price = q1_price - 1.5 * IQR_price

print('Limite superior de price: ', sup_price)
print('Limite inferior de price: ', inf_price)

# verificando o conjunto original da variável price
fig, ax = plt.subplots(figsize=(15,3))
df.price.plot(kind='box', vert=False);
ax.set_title('Dataset Original - Price')
plt.show()
print("O dataset possui total de {} entradas.".format(df.shape[0]))
print("A coluna Price possui {} entradas acima de 295.0.".format(len(df[df.price > 295.0])))
print("Isto representa {:.2f}% do dataset.".format((len(df[df.price > 295.0]) / df.shape[0])*100))

# identificando os outliers para a variável minimum_nights
q1_minimum_nights = df.minimum_nights.quantile(.25)
q3_minimum_nights = df.minimum_nights.quantile(.75)
IQR_minimum_nights = q3_minimum_nights - q1_minimum_nights
print('IQR da variável minimum_nights: ', IQR_minimum_nights)

# definindo os limites para a variável Price                                              
sup_minimum_nights = q3_minimum_nights + 1.5 * IQR_minimum_nights
inf_minimum_nights = q1_minimum_nights - 1.5 * IQR_minimum_nights

print('Limite superior de minimum_nights: ', sup_minimum_nights)
print('Limite inferior de minimum_nights: ', inf_minimum_nights)

# verificando o conjunto original da variável minimum_nights
fig, ax = plt.subplots(figsize=(15,3))
df.minimum_nights.plot(kind='box', vert=False);
ax.set_title('Dataset Original - minimum_nights')
plt.show()
print("O dataset possui total de {} entradas.".format(df.shape[0]))
print("A coluna minimum_nights possui {} entradas acima de 6.0.".format(len(df[df.minimum_nights > 6.0])))
print("Isto representa {:.2f}% do dataset.".format((len(df[df.minimum_nights > 6.0]) / df.shape[0])*100))

"""Como podemos ver na variável `price`, apesar de não termos outliers na parte inferior, continuamos tendo valores iguais a zero, que precisam ser tratados.

Vamos tratar os dados que estão acima dos limites superiores calculados para `price` e `minimum_nights`assim com os valores que apresentam zero para `price`.

**Removendo os outliers das variáveis `price` e `minimum_nights`**
"""

# limpando o dataset
df_clean = df.copy()

df_clean.drop(df_clean[df_clean.price > 295.0].index, axis=0, inplace=True)
df_clean.drop(df_clean[df_clean.price == 0.0].index, axis=0, inplace=True)
df_clean.drop(df_clean[df_clean.minimum_nights > 6.0].index, axis=0, inplace=True)

print('Shape antes da limpeza: ', df.shape)
print('Shape após a limpeza: ',df_clean.shape)

"""**Visualizando e analisando os dados tratados**

Para garantirmos que não estamos lidando com outliers que vão prejudicar nossa análise, vamos checar os histogramas novamente.
"""

# verificando as distribuições
df_clean.hist(figsize=(15,10), grid=False);

# verificando a distribuição estatística dos dados limpos
df_clean.describe().round(1)

"""Agora conseguimos ter uma ideia bem melhor da distribuição dos nossos dados.

Alguns destaques:

* A mediana das variáveis `price` e `minimum_nights` foram pouquíssimas afetadas pela limpeza dos outliers, mostrando mais uma vez a robustez desse atributo como solução para dados ausentes;
* A média da variável `price` e `minimum_nights` foram reduzidas drasticamente, enfatizando a sensibilidade desse atributo em relação aos outliers;
* Agora, temos dados que respeitam as regras definidas no início do notebook, onde vimos o que são bons dados.

### **Tipo de imóvel mais alugado do Airbnb em Roma**

Os anfitriões do Airbnb podem listar casas/apartamentos inteiros, quartos privados, compartilhados e, mais recentemente, quartos de hotel.

Dependendo do tipo de quarto e atividade, uma listagem residencial do Airbnb poderia ser mais como um hotel, disruptiva para os vizinhos, tirando moradias e ilegalmente.
"""

# agrupando quantidade de cada tipo de imóveis e classificando
y = df_clean.room_type.value_counts().sort_values()

# gerando os elementos do gráfico de barras
fig, ax = plt.subplots(figsize=(10,5))
y.plot(y=y, kind="barh", ax=ax, color=["gray","gray","gray","#253750"])
plt.title("Quantidade de imóveis disponíveis", fontsize=23, pad=30, loc="left")
plt.suptitle("Agrupado por tipo de imóvel", fontsize=15, x=0.135, y=0.88, ha="left")

# adicionando valores nas barras
for index, value in enumerate(y): 
    plt.text(value, index, str(value), color="black", verticalalignment="center", fontsize=14) 

# removendo visibilidade do fundo
for item in [fig, ax]:
    item.patch.set_visible(False)

# definindo visibilidade de parâmetros
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False) 
plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=True) 
for pos in ['right', 'top', 'bottom', 'left']: 
    plt.gca().spines[pos].set_visible(False)

# plotado gráfico
fig.tight_layout()
plt.show()

# agrupando porcentagem de cada tipo de imóveis e classificando
y = (df_clean.room_type.value_counts().sort_values()/ df_clean.shape[0])

# arredondando valores
y = round(y, 2)

# gerando os elementos do gráfico de barras
fig, ax = plt.subplots(figsize=(10,5))
y.plot(y=y, kind="barh", ax=ax, color=["gray", "gray", "gray", "#253750"])
plt.title("Porcentagem de imóveis disponíveis", fontsize=23, pad=30, loc="left")
plt.suptitle("Agrupado por tipo de imóvel", fontsize=15, x=0.135, y=0.88, ha="left")

# adicionando valores nas barras
for index, value in enumerate(y): 
    plt.text(value, index, str(value), color="black", verticalalignment="center", fontsize=14) 

# removendo visibilidade do fundo
for item in [fig, ax]:
    item.patch.set_visible(False)

# definindo visibilidade de parâmetros
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False) 
plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=True) 
for pos in ['right', 'top', 'bottom', 'left']: 
    plt.gca().spines[pos].set_visible(False)

# plotado o gráfico
fig.tight_layout()
plt.show()

"""### **Média dos preços de aluguel por tipo de imóvel**

A coluna da variável `room_type` indica o tipo de locação que está anunciada no Airbnb. Se você já alugou no site, sabe que existem opções de apartamentos/casas inteiras, apenas o aluguel de um quarto ou mesmo dividir o quarto com outras pessoas.

Vamos agrupar `room_type` e calcular a média de valores para cada tipo de imóvel, usando o método `groupby()` e o `mean()`.
"""

# média de preço para cada tipo de imóveis e classificando
y_price = df_clean.groupby('room_type').price.mean().sort_values()

# arredondando valores
y_price = round(y_price, 2)

# gerando os elementos do gráfico de barras
fig, ax = plt.subplots(figsize=(10,5))
y_price.plot(y=y_price, kind="barh", ax=ax, color=["gray", "gray", "#253750", "#253750"])
plt.title("Média dos preços de aluguel", fontsize=23, pad=30, loc="left")
plt.suptitle("Agrupado por tipo de imóvel", fontsize=15, x=0.158, y=0.88, ha="left")

# adicionando valores nas barras
for index, value in enumerate(y_price): 
    plt.text(value, index, str(value), color="black", verticalalignment="center", fontsize=14) 

# removendo visibilidade do fundo
for item in [fig, ax]:
    item.patch.set_visible(False)

# definindo visibilidade de parâmetros
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False) 
plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=True) 
for pos in ['right', 'top', 'bottom', 'left']: 
    plt.gca().spines[pos].set_visible(False)

# plotado o gráfico
fig.tight_layout()
plt.show()

"""### **Qual a localidade mais cara do Airbnb em Roma?**

Uma maneira de se verificar uma variável em função da outra é usando groupby(). No caso, queremos comparar os bairros (neighbourhoods) a partir do preço de locação.
"""

# média de preço dos 10 bairros mais caros
y_neighbourhood = df_clean.groupby(['neighbourhood']).price.mean().sort_values(ascending=False)[:10]

# arredondando valores
y_neighbourhood = round(y_neighbourhood, 2)

# gerando os elementos do gráfico de barras
fig, ax = plt.subplots(figsize=(12,7))
y_neighbourhood.plot(y=y_neighbourhood, kind="barh", ax=ax, color=["#253750", "gray", "gray", "gray", "gray", "gray", "gray", "gray", "gray", "gray"])
plt.title("Média dos preços dos bairros", fontsize=23, pad=30, loc="left")
plt.suptitle("10 mais caros", fontsize=15, x=0.1876, y=0.910, ha="left")

# adicionando valores nas barras
for index, value in enumerate(y_neighbourhood): 
    plt.text(value, index, str(value), color="black", verticalalignment="center", fontsize=12) 

# removendo visibilidade do fundo
for item in [fig, ax]:
    item.patch.set_visible(False)

# definindo visibilidade de parâmetros
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False) 
plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=True) 
for pos in ['right', 'top', 'bottom', 'left']: 
    plt.gca().spines[pos].set_visible(False)

# plotado gráfico
fig.tight_layout()
plt.show()

df_clean['neighbourhood'].unique()

"""Acima, vemos que o bairro `I Centro Storico` apresenta uma média de preço bem superior aos demais lugares.

Verificando sites especializados para buscar uma explicação para tal diferença, foi possível verificar no site [Buenasdicas]('https://www.buenasdicas.com/onde-ficar-em-roma-6597/'), que este bairro apresenta maior concentração de pontos turístico, o que nos leva à entender o porquê desta discrepância de preço no Airbnb.

### **Frequência de minimum_nights para cada categoria de dias?**
"""

# ver a média da coluna `minimum_nights``
y_minimum = df_clean.groupby('minimum_nights').minimum_nights.sum()

# arredondando valores
y_minimum = round(y_minimum, 0)

# gerando os elementos do gráfico de barras
fig, ax = plt.subplots(figsize=(10,5))
y_minimum.plot(x=y_minimum, kind="barh", ax=ax, color=["#253750", "#253750", "#253750", "gray", "gray", "gray", "gray"])

plt.title("Frequência de minimum_nights", fontsize=23, pad=30, loc="left")
plt.suptitle("Agrupado por minimum_nights de 0 à 6 dias", fontsize=15, x=0.055, y=0.88, ha="left")

# adicionando valores nas barras
for index, value in enumerate(y_minimum): 
    plt.text(value, index, str(value), color="black", verticalalignment="center", fontsize=14) 

# removendo visibilidade do fundo
for item in [fig, ax]:
    item.patch.set_visible(False)

# definindo visibilidade de parâmetros
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False) 
plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=True) 
for pos in ['right', 'top', 'bottom', 'left']: 
    plt.gca().spines[pos].set_visible(False)

# plotado o gráfico
fig.tight_layout()
plt.show()

"""Como pode-se observar, a quantidade mais frequente de `minimum_nights` dentre os imóveis disponíveis no Airbnb são de 2 dias, 3 dias e 1 dia. Ou seja, dentre diversos imóveis listados no dataset, estes dias listados anteriormente serão os mais frequente no momento da seleção.

### **Verificando correlações existentes entre as variáveis do dataset**

**Correlação** significa que existe uma relação entre duas coisas. No nosso contexto, estamos buscando relação ou semelhança entre duas variáveis.

Essa relação pode ser medida, e é função do coeficiente de correlação estabelecer qual a intensidade dela. Para identificar as correlações existentes entre as variáveis de interesse, vou:

* Criar uma matriz de correlação;
* Gerar um *heatmap* a partir dessa matriz, usando a biblioteca `seaborn`.

Antes de efetivamente verificar as correlações, vamos simplificar esta tarefa, unindo informações e removendo as informações redundantes como número de avaliações que possue três métricas relativamente parecidas.

A seguir, unimos as métricas latitude e longitude em uma só métrica que é a distância ao centro de Roma.
"""

# Calculando a latitude média da região central
latitude_centro = df_clean[df_clean['neighbourhood'] == 'I Centro Storico'].latitude.mean()

# Calculando a longitude média da região central
longitude_centro = df_clean[df_clean['neighbourhood'] == 'I Centro Storico'].longitude.mean()

# Calculando a distância euclidiana das coordenadas médias das locações da região central
df_clean['distancia_centro'] = (df_clean['latitude'] - latitude_centro)**2 + (df_clean['longitude'] - longitude_centro)**2

"""Vamos criar uma matriz que demonstra a correlação entre as variévais definidas."""

# criar uma matriz de correlação
corr = df_clean[[
    'price',
    'minimum_nights', 
    'number_of_reviews',
    'calculated_host_listings_count', 
    'availability_365', 
    'distancia_centro'
    ]].corr()

# mostrar a matriz de correlação
display(corr)

# plotar um heatmap a partir das correlações
sns.set(rc = {'figure.figsize':(10,7)})
sns.heatmap(corr, cmap='RdBu', fmt='.2f', square=True, linecolor='white', annot=True);

"""A maior correlação encontrada com relação à variável alvo foi de 0.18 que é uma correlação entre número de dias de disponibilidade dentro de 365 dias que o locatário tem no dataset e o preço. 

A segunda maior correlação encontrada com relação à variável alvo foi de 0.16 que é uma correlação entre a quantidade de imóveis do mesmo anfitrião e o preço.

Outra correlação encontrada é a relação da distância do centro com o preço, que apresentou valor -0.15, o que indica que quanto maior a distância ao centro menor tende a ser o preço, as demais correlações encontradas com a variável alvo são pouco relevantes.

### **Visualização do dataset em mapas**

Folium é uma biblioteca que permite visualizações interativas de mapas em Python, com esta biblioteca vamos examinar algumas características do dataset de Roma disponibilidado pelo Airbnb.

Primeiramente vamos carregar nossos dados e examiná-los brevemente, como fizemos antes.
"""

# carregando os dados
df_clean.head()

"""**HeatMap**

Para uma melhor compreensão da densidade de listagens, podemos usar o mapa de calor folium.
"""

# plotando o mapa
map_folium = folium.Map([41.8940108,12.3968282],zoom_start=10)
HeatMap(df_clean[['latitude','longitude']].dropna(),radius=8,gradient={0.2:'blue',0.4:'purple',0.6:'orange',1.0:'red'}).add_to(map_folium)
display(map_folium)

"""Do mapa acima, podemos ver claramente onde está localizada a lista mais densa, mostrada pela cor vermelha na área central. A densidade de listagem diminui cada vez mais, quanto mais está mais distante da região central.

**Fast Marker Cluster**
"""

coord = df_clean.loc[:,['longitude','latitude']]
coord.describe()

"""Abaixo, você pode ver que a maioria dos anúncios estão no centro da cidade. Este mapa é interativo e você pode ampliar os clusters para encontrar os locais individuais das listagens."""

# Commented out IPython magic to ensure Python compatibility.
# %pip install branca==0.3.1 

# plotando o mapa
lats = df_clean['latitude'].tolist()
lons = df_clean['longitude'].tolist()
locations = list(zip(lats, lons))

map1 = folium.Map(location=[41.8940108,12.3968282], zoom_start=11)
FastMarkerCluster(data=locations).add_to(map1)
map1

"""**Price Map**

Em seguida, visualizamos o mapa de gráfico de dispersão de cada listagem e a diferença na faixa de preço usando pontos de longitude e latitude com um mapa de calor de preço.

"""

# import our image 
rome_img = mpimg.imread('/content/rome.png')
# plot the data
ax = df_clean.plot(
    kind="scatter", 
    x='longitude', 
    y='latitude', 
    figsize=(20,8),
    c="price", 
    cmap=plt.get_cmap("jet"),
    colorbar=True, 
    alpha=0.4,
)
# use our map with it's bounding coordinates
plt.imshow(rome_img, extent=[12.115064, 12.744020, 41.717653, 41.995721], alpha=1.0)            
# add axis labels
plt.ylabel("Latitude", fontsize=10)
plt.xlabel("Longitude", fontsize=10)
# set the min/max axis values - these must be the same as above
plt.xlim(12.115064, 12.744020)
plt.ylim(41.717653, 41.995721)
plt.legend(fontsize=10)
plt.show()

"""Acima, pode-se ver que o preços mais altos dos anúncios estão mais concentrado no centro da cidade.

## Conclusões

### **REVISAR A CONCLUSÃO**


Foi feita apenas uma análise superficial na base de dados do Airbnb, porém já se percebeu que existem *outliers* em algumas das variáveis. 

Também se notou que em algumas localidades há poucos imóveis disponíveis, o que pode distorcer as informações estatísticas de alguns atributos.

Por fim, lembra-se que este *dataset* é uma versão resumida, ideal apenas para uma abordagem inicial. Recomenda-se que seja usado, em uma próxima análise exploratória, o conjunto de dados completos, com 106 atributos disponíveis.
"""