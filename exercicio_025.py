#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de 
#idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, 
#adulta ou idosa, conforme a média calculada.

numero_pessoas = int(input("Digite o numero de notas que deseja ser calculado: "))
soma_idades = 0
for i in range (numero_pessoas):
    nota = float(input("Digite a {}° nota: ".format(i + 1)))
    soma_idades += nota
media = soma_idades/numero_pessoas
print(f"A media das {numero_pessoas} pessoas é de: {media}")
if media >= 0 and media < 25:
    print("A turma é jovem")
if media >= 26 and media < 60:
    print("A turma é adulta")
if media > 60:
    print("A turma é idosa")