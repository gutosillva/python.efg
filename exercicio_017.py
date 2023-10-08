#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

fatorial_usuario = int(input("Digite um numero inteiro positivo: "))

if fatorial_usuario < 0:
    print("Valor invalido")
if fatorial_usuario == 0:
    print("A fatorial de 0 é igual a 1")
else:
    fatorial = 1 
    for i in range(1, fatorial_usuario + 1):
        fatorial *= i
    print(f"{fatorial_usuario}! = {fatorial}")