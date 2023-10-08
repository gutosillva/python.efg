#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, 
#o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a 
#er pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
# Define o preço do litro da gasolina e do álcool
preco_gasolina = 2.50
preco_alcool = 1.90

# Solicita ao usuário o número de litros vendidos e o tipo de combustível
litros_vendidos = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A para álcool, G para gasolina): ").upper()

# Calcula o valor a ser pago pelo cliente
if tipo_combustivel == 'A':
    if litros_vendidos <= 20:
        valor_pagar = litros_vendidos * (preco_alcool - (preco_alcool * 0.03))
    else:
        valor_pagar = litros_vendidos * (preco_alcool - (preco_alcool * 0.05))
elif tipo_combustivel == 'G':
    if litros_vendidos <= 20:
        valor_pagar = litros_vendidos * (preco_gasolina - (preco_gasolina * 0.04))
    else:
        valor_pagar = litros_vendidos * (preco_gasolina - (preco_gasolina * 0.06))
else:
    print("Tipo de combustível inválido. Use 'A' para álcool ou 'G' para gasolina.")
    valor_pagar = None

# Exibe o valor a ser pago pelo cliente
if valor_pagar is not None:
    print(f"Valor a ser pago: R$ {valor_pagar:.2f}")
