#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
produto1=int(input("Valor do 1° produto:"))
produto2=int(input("Valor do 2° produto:"))
produto3=int(input("Valor do 3° produto:"))
if produto1 < produto2 and produto1 < produto3:
    print("você deve comprar o 1° prodduto.")
    
if produto2 < produto1 and produto2 < produto3:
    print("você deve comprar o 2° prodduto.")
    
if produto3 < produto2 and produto3 < produto1:
    print("você deve comprar o 3° prodduto.")


# Crie uma lista para armazenar os valores dos produtos
produtos = []

# Solicite ao usuário para inserir os valores dos produtos
for i in range(1, 4):
    valor = float(input(f"Valor do {i}° produto: "))
    produtos.append(valor)

# Encontre o índice do produto mais barato na lista
indice_menor_valor = produtos.index(min(produtos))

# Use uma única estrutura condicional para determinar qual produto comprar
if indice_menor_valor == 0:
    print("Você deve comprar o 1° produto.")
elif indice_menor_valor == 1:
    print("Você deve comprar o 2° produto.")
else:
    print("Você deve comprar o 3° produto.")
	
#
#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, s
#abendo que a decisão é sempre pelo mais barato.
produto1=int(input("Valor do 1° produto:"))
produto2=int(input("Valor do 2° produto:"))
produto3=int(input("Valor do 3° produto:"))
if produto1 < produto2 and produto1 < produto3:
    print("você deve comprar o 1° prodduto.")
    
if produto2 < produto1 and produto2 < produto3:
    print("você deve comprar o 2° prodduto.")
    
if produto3 < produto2 and produto3 < produto1:
    print("você deve comprar o 3° prodduto.")