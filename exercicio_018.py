#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

conjunto = int(input("Digite a quantidade de numeros do conjunto: "))

valor_menor = float('inf')
valor_maior = float('-inf')
soma_valores = 0

for i in range(conjunto):
    numero = float(input(f"Digite o {i + 1}º número: "))
    soma_valores += numero
    if numero < valor_menor:
        valor_menor = numero
    if numero > valor_maior:
        valor_maior = numero

print(f"menor valor: {valor_menor}")
print(f"maior valor: {valor_maior}")
print(f"soma dos valores: {soma_valores}")
