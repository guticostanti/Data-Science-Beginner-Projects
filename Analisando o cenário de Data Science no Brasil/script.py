# importar as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
 
# melhorar a visualização
pd.set_option('max_columns',170)
#%matplotlib inline
#%config InlineBackend.figure_format = 'svg'
 
# importar o dataset para um DataFrame
df = pd.read_csv('datahackers-survey-2019-anonymous-responses.csv')
 
# extrair o nome da variável da tupla
df.columns = [eval(col)[1] for col in df.columns]

#...............................................................................
# countplot de estado onde mora
plt.figure(figsize=(15,10))
ax = sns.countplot(x="living_state", data=df[df['is_data_science_professional'] == 1], order=df['living_state'].value_counts().index)
plt.title('Cientistas de Dados por Estado', size=14)
plt.xlabel('Estados', size=12)
plt.show()


#...................................................................................
# plotar gráfico de gêneros
plt.figure(figsize=(8,8))
ax = sns.countplot(x="gender", data=df[df['is_data_science_professional'] == 1], order=df['gender'].value_counts().index)
plt.title('Cientistas de Dados por Gênero', size=14)
plt.xlabel('Gênero', size=12)
plt.show()

#.................................................................................
# ver formação dos profissionais de data science
plt.figure(figsize=(18,10))
ax = sns.countplot(x="degreee_level", data=df[df['is_data_science_professional'] == 1], order=df['degreee_level'].value_counts().index)
plt.title('Cientistas de Dados por Nível Educacional', size=14)
plt.xlabel('Nível Educacional', size=12)
plt.show()

#.................................................................................
# plotar histograma de idade
plt.figure(figsize=(12,6))
ax = sns.distplot(df.age)
plt.title('Cientistas de Dados por Idade', size=14)
plt.xlabel('Idade', size=12)
plt.show()

#.................................................................................
ordem_salarios = ["Menos de R$ 1.000/mês",
         "de R$ 1.001/mês a R$ 2.000/mês",
         "de R$ 2.001/mês a R$ 3000/mês",
         "de R$ 3.001/mês a R$ 4.000/mês",
         "de R$ 4.001/mês a R$ 6.000/mês",
         "de R$ 6.001/mês a R$ 8.000/mês",
         "de R$ 8.001/mês a R$ 12.000/mês",
         "de R$ 12.001/mês a R$ 16.000/mês",
         "de R$ 16.001/mês a R$ 20.000/mês",
         "de R$ 20.001/mês a R$ 25.000/mês"]
 
labels = ["Menos de R\$ 1.000",
         'de R\$ 1.001 a R\$ 2.000',
         "de R\$ 2.001 a R$ 3.000",
         "de R\$ 3.001 a R\$ 4.000",
         "de R\$ 4.001 a R\$ 6.000",
         "de R\$ 6.001 a R\$ 8.000",
         "de R\$ 8.001 a R\$ 12.000",
         "de R\$ 12.001 a R\$ 16.000",
         "de R\$ 16.001 a R\$ 20.000",
         "de R\$ 20.001 a R\$ 25.000"]
 
# plotar o gráfico de salários
ax = sns.countplot(df[df['is_data_science_professional'] == 1].salary_range, order=ordem_salarios)
ax.set_xticklabels(labels=labels, rotation=45, horizontalalignment='right')
plt.show()

#.........................................................................................
# plotar linguagens mais usadas
plt.figure(figsize=(10,5))
ax = sns.countplot(x="most_used_proggraming_languages",
                   data=df.replace("Não utilizo nenhuma das linguagens listadas", "N.D.A."))
plt.title('Cientistas de Dados por Linguagem de Programação Mais Utilizada', size=14)
plt.xticks(rotation= 45,horizontalalignment='right')
plt.xlabel('Linguagem de Programação Mais Utilizada', size=12)
plt.show()
