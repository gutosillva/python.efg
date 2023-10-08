#Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
#Dica: utilize uma função de arredondamento.
# Solicita ao usuário que digite um número
numero = float(input("Digite um número: "))

# Arredonda o número para o inteiro mais próximo
numero_arredondado = round(numero)

# Verifica se o número é igual ao seu arredondamento
if numero == numero_arredondado:
    print(f"O número {numero} é um número inteiro.")
else:
    print(f"O número {numero} é um número decimal.")
