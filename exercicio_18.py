#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
# Solicita ao usuário que digite uma data no formato dd/mm/aaaa
data = input("Digite uma data no formato dd/mm/aaaa: ")

# Divide a entrada em dia, mês e ano
dia, mes, ano = map(int, data.split('/'))

# Define uma lista com o número máximo de dias por mês
dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Verifica se o ano é bissexto e atualiza o número de dias de fevereiro se for
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    dias_por_mes[2] = 29

# Verifica se o mês e o dia estão dentro dos limites válidos
if 1 <= mes <= 12 and 1 <= dia <= dias_por_mes[mes]:
    print("Data válida.")
else:
    print("Data inválida.")
