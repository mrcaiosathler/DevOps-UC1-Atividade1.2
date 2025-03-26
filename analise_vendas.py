import pandas as pd

#Carregar dados de vendas
dados = pd.read_csv("data/vendas.csv")

#Calcular total de vendas
total_vendas = dados["valor"].sum()
print(f"Total de Vendas: R${total_vendas:.2f}")