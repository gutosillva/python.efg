#Numa eleição existem três candidatos. 
#Faça um programa que peça o número total de eleitores. 
#Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

candidato_1 = 0
candidato_2 = 0
candidato_3 = 0

eleitor = int(input("Quantos eleitores irão votar: "))
for i in range (eleitor):
    voto = float(input("Digite o voto do {}° eleitor (1- candidato A; 2- candidato B; 3- candidato C): ".format(i + 1)))
    if voto == 1:
        candidato_1 += 1
    if voto == 2:
        candidato_2 += 1
    if voto == 3: 
        candidato_3 += 1
    elif voto > 3:
        print("Voto invalido")
        exit()
quant_voto = candidato_1 + candidato_2 + candidato_3
print("Quantidade de votos do 1° candidato:",candidato_1)
print("Quantidade de votos do 2° candidato:",candidato_2)
print("Quantidade de votos do 3° candidato:",candidato_3)
print("Quantidade de eleitores:",eleitor)
print("Quantidade de votos computados:", quant_voto)

        