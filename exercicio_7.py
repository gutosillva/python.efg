#Faça um Programa que leia três números e mostre o maior e o menor deles.
# Solicita ao usuário que digite três números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Inicializa as variáveis para armazenar o maior e o menor número
maior_numero = numero1
menor_numero = numero1

# Verifica se o segundo número é maior que o atual maior número
if numero2 > maior_numero:
    maior_numero = numero2

# Verifica se o segundo número é menor que o atual menor número
if numero2 < menor_numero:
    menor_numero = numero2

# Verifica se o terceiro número é maior que o atual maior número
if numero3 > maior_numero:
    maior_numero = numero3

# Verifica se o terceiro número é menor que o atual menor número
if numero3 < menor_numero:
    menor_numero = numero3

# Exibe o maior e o menor número
print(f"O maior número é {maior_numero}")
print(f"O menor número é {menor_numero}")
