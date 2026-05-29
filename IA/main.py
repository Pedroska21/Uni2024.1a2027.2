from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd

# produtos: mochila = 1, tenis = 2, viseira = 3
# ordem: produto, estoque, preço
csv = pd.read_csv('dados.csv', sep=";")
csv = csv.dropna()

le = LabelEncoder()
csv['produto'] = le.fit_transform(csv['produto'])

dados = csv.values

atributos = dados [:,0:2]
preco = dados[:,2]

modelo = LinearRegression()
modelo.fit(atributos, preco)

#novos produtos

produto = int(input('informe o tipo de produto mochila[1] tenis[2] viseira[3]'))
estoque = int(input('quantidade no estoque:'))

retorno = modelo.predict([[produto, estoque]])
print('preço sugerido: ', float(retorno[0]))