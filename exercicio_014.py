#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade 
#de números pares e a quantidade de números impares.
quant_par = 0
quant_impar = 0
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))

    if numero % 2 == 0:
        quant_par += 1
    else:
        quant_impar += 1
print(f"São {quant_par} numeros pares")
print(f"São {quant_impar} numeros impares")