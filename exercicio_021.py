#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
#Um número primo é aquele que é divisível somente por ele mesmo e por 1.

numero = int(input("Digite um número inteiro qualquer: "))

# Verificar se o número é maior que 1
if numero > 1:
    # Loop para verificar divisibilidade
    for i in range(2, numero):
        if (numero % i) == 0:
            print("Não é um número primo")
            break
    else:
        print("É um número primo")
else:
    print("Não é um número primo")
