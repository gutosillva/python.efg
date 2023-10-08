#Faça um programa que calcule o valor total investido por um colecionador 
#em sua coleção de CDs e o valor médio gasto em cada um deles. 
#O usuário deverá informar a quantidade de CDs e o valor para em cada um.

CDs = int(input("Digite a quantidade de CDs que há em sua coleção: "))
soma_cds = 0

for i in range(CDs):
    preco = float(input(f"Digite o valor do {i+1}° CD: "))
    soma_cds += preco
valor_medio = soma_cds / CDs
print(f"O valor total gasto por você nos CDs é: R${round(soma_cds,2)}")
print(f"O valor medio gasto em cada CD é de: R${round (valor_medio,2)}")