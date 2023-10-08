#Faça um programa que calcule o mostre a média aritmética de N notas.

numero = int(input("Digite o numero de notas que deseja ser calculado: "))
soma_notas = 0
for i in range (numero):
    nota = float(input("Digite a {}° nota: ".format(i + 1)))
    soma_notas += nota
media = soma_notas/numero
print(f"A media das {numero} é: {media}")