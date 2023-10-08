#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                     # Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
#porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente 
#receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de 
#carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
#tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

# Solicita ao usuário o tipo de carne e a quantidade em Kg
print("Tipos de carne disponíveis:")
print("1 - File Duplo")
print("2 - Alcatra")
print("3 - Picanha")
tipo_carne = int(input("Escolha o tipo de carne (1/2/3): "))
quantidade = float(input("Digite a quantidade em Kg: "))

# Define os preços por Kg de cada tipo de carne
preco_file_duplo = 4.90
preco_alcatra = 5.90
preco_picanha = 6.90

# Calcula o preço total com base no tipo de carne e na quantidade
if tipo_carne == 1:
    preco_total = quantidade * preco_file_duplo
    tipo_carne_nome = "File Duplo"
elif tipo_carne == 2:
    preco_total = quantidade * preco_alcatra
    tipo_carne_nome = "Alcatra"
elif tipo_carne == 3:
    preco_total = quantidade * preco_picanha
    tipo_carne_nome = "Picanha"
else:
    print("Tipo de carne inválido.")
    preco_total = 0
    tipo_carne_nome = ""

# Solicita ao usuário o tipo de pagamento (dinheiro ou cartão Tabajara)
tipo_pagamento = input("Digite o tipo de pagamento (D para dinheiro, C para cartão Tabajara): ").upper()

# Aplica o desconto de 5% se o pagamento for com cartão Tabajara
if tipo_pagamento == "C":
    desconto = preco_total * 0.05
else:
    desconto = 0

# Calcula o valor a pagar após aplicar o desconto
valor_a_pagar = preco_total - desconto

# Exibe o cupom fiscal
print("\nCUPOM FISCAL")
print(f"Tipo de carne: {tipo_carne_nome}")
print(f"Quantidade: {quantidade} Kg")
print(f"Preço total: R$ {preco_total:.2f}")
print(f"Tipo de pagamento: {'Cartão Tabajara' if tipo_pagamento == 'C' else 'Dinheiro'}")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
