#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, 
#por quais número ele é divisível.
numero = int(input("Digite um número inteiro qualquer: "))

# Verificar se o número é maior que 1
if numero > 1:
    divisores = []  # Lista para armazenar os divisores
    # Loop para verificar divisibilidade
    for i in range(2, numero):
        if (numero % i) == 0:
            divisores.append(i)
    
    if not divisores:  # Se a lista de divisores estiver vazia, é primo
        print("É um número primo")
    else:
        print("Não é um número primo. É divisível por:", divisores)
else:
    print("Não é um número primo")
