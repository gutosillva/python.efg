#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
#O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Solicita ao usuário que digite o valor do saque
valor_saque = int(input("Digite o valor do saque (entre 10 e 600 reais): "))

# Verifica se o valor do saque está dentro dos limites válidos
if valor_saque < 10 or valor_saque > 600:
    print("Valor de saque inválido. O valor deve estar entre 10 e 600 reais.")
else:
    # Inicializa as variáveis para contar as notas
    notas_100 = 0
    notas_50 = 0
    notas_10 = 0
    notas_5 = 0
    notas_1 = 0

    # Calcula a quantidade de notas de cada valor
    while valor_saque >= 100:
        notas_100 += 1
        valor_saque -= 100

    while valor_saque >= 50:
        notas_50 += 1
        valor_saque -= 50

    while valor_saque >= 10:
        notas_10 += 1
        valor_saque -= 10

    while valor_saque >= 5:
        notas_5 += 1
        valor_saque -= 5

    while valor_saque >= 1:
        notas_1 += 1
        valor_saque -= 1

    # Exibe a quantidade de notas de cada valor fornecidas
    if notas_100 > 0:
        print(f"Notas de 100 reais: {notas_100}")
    if notas_50 > 0:
        print(f"Notas de 50 reais: {notas_50}")
    if notas_10 > 0:
        print(f"Notas de 10 reais: {notas_10}")
    if notas_5 > 0:
        print(f"Notas de 5 reais: {notas_5}")
    if notas_1 > 0:
        print(f"Notas de 1 real: {notas_1}")
