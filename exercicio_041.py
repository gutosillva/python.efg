#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 
#valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
#Os juros e a quantidade de parcelas seguem a tabela abaixo:
#Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
#1       0
#3       10
#6       15
#9       20
#12      25

def calcular_parcela(divida, juros, parcelas):
    valor_juros = divida * (juros / 100)
    valor_total = divida + valor_juros
    valor_parcela = valor_total / parcelas
    return valor_juros, valor_parcela

tabela_pacelas = [
    (1, 0),
    (3, 10),
    (6, 15),
    (9, 20),
    (12, 25)
]

divida = float(input("Qual valor da divida: R$ "))
print("\nTabela de parcelas: ")
print("Pacelas\tJuros\t\tValor da Parcela")

for parcelas, juros in tabela_pacelas:
    valor_juros, valor_parcela = calcular_parcela(divida, juros, parcelas)
    print(f"{parcelas}\t\t{juros}%\t\tR$ {valor_parcela:.2f} (Juros: R$ {valor_juros:.2f})")