#Faça um Programa que leia três números e mostre-os em ordem decrescente.
# Solicita ao usuário que digite três números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Cria uma lista com os números
numeros = [numero1, numero2, numero3]

# Ordena a lista em ordem decrescente
numeros.sort(reverse=True)

# Exibe os números em ordem decrescente
print("Números em ordem decrescente:")
for numero in numeros:
    print(numero)
