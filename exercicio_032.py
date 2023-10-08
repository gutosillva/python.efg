#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
#Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
#Fatorial de: 5
#5! =  5 . 4 . 3 . 2 . 1 = 120

numero = int(input("Digite um número inteiro: "))
if numero < 0:
    print("O fatorial não está definido para números negativos.")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"Fatorial de: {numero}")
    print(f"{numero}! =", end=" ")
    for i in range(1, numero):
        print(f"{i} .", end=" ")
    print(f"{numero} =", fatorial)