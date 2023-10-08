#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                     # Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
#receberá ainda um desconto de 10% sobre este total. 
#Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) 
#de maças adquiridas e escreva o valor a ser pago pelo cliente.

# Solicita ao usuário a quantidade de morangos e maçãs em Kg
quantidade_morangos = float(input("Digite a quantidade de morangos (em Kg): "))
quantidade_macas = float(input("Digite a quantidade de maçãs (em Kg): "))

# Calcula o preço dos morangos e maçãs de acordo com a tabela de preços
if quantidade_morangos <= 5:
    preco_morangos = quantidade_morangos * 2.50
else:
    preco_morangos = quantidade_morangos * 2.20

if quantidade_macas <= 5:
    preco_macas = quantidade_macas * 1.80
else:
    preco_macas = quantidade_macas * 1.50

# Calcula o valor total da compra
valor_total = preco_morangos + preco_macas

# Aplica o desconto de 10% se o cliente comprar mais de 8 Kg ou ultrapassar R$ 25,00
if (quantidade_morangos + quantidade_macas > 8) or (valor_total > 25):
    desconto = valor_total * 0.10
    valor_total -= desconto

# Exibe o valor a ser pago pelo cliente
print(f"Valor a ser pago: R$ {valor_total:.2f}")
