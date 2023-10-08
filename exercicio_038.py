#Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
#Faça um programa que determine o salário atual desse funcionário. Após concluir isto, 
#altere o programa permitindo que o usuário digite o salário inicial do funcionário.

salario_inicial = 1000
ano_inicial = 1995
ano_final = 2023
porcentagem = 1.5 / 100

while ano_inicial <= ano_final:
    aumento_anual = salario_inicial * (1 + porcentagem)
    porcentagem *= 2
    ano_inicial += 1
    salario_inicial = aumento_anual 
    print(f"Ano: {ano_inicial - 1}, Salário: R$ {aumento_anual:.2f}")


###################################################################################
salario_inicial = float(input("Digite o salário inicial do funcionário em 1995: "))
ano = 1995
percentual_aumento = 1.5 / 100  
ano_atual = 2023
while ano <= ano_atual:
    salario_inicial = salario_inicial * (1 + percentual_aumento) 
    percentual_aumento *= 2  
    ano += 1
print(f"O salário atual em {ano_atual} é R$ {salario_inicial:.2f}")
