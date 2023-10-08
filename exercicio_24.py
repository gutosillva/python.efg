#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.
# Solicita ao usuário que digite dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Solicita ao usuário que escolha uma operação
print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
escolha = int(input("Digite o número da operação desejada: "))

# Realiza a operação selecionada
if escolha == 1:
    resultado = numero1 + numero2
    operacao = "soma"
elif escolha == 2:
    resultado = numero1 - numero2
    operacao = "subtração"
elif escolha == 3:
    resultado = numero1 * numero2
    operacao = "multiplicação"
elif escolha == 4:
    resultado = numero1 / numero2
    operacao = "divisão"
else:
    print("Operação inválida.")
    resultado = None

# Verifica se o resultado é par ou ímpar
par_impar = "par" if resultado % 2 == 0 else "ímpar"

# Verifica se o resultado é positivo ou negativo
positivo_negativo = "positivo" if resultado >= 0 else "negativo"

# Verifica se o resultado é inteiro ou decimal
inteiro_decimal = "inteiro" if resultado.is_integer() else "decimal"

# Exibe o resultado da operação e as informações sobre o resultado
if resultado is not None:
    print(f"O resultado da {operacao} é {resultado:.2f}, que é {par_impar}, {positivo_negativo} e {inteiro_decimal}.")
