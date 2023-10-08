#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. 
# Solicita ao usuário que digite um número inteiro menor que 1000
numero = int(input("Digite um número inteiro menor que 1000: "))

# Verifica se o número está dentro do intervalo válido
if numero < 0 or numero >= 1000:
    print("Número fora do intervalo válido.")
else:
    # Separa as centenas, dezenas e unidades do número
    centenas = numero // 100
    dezenas = (numero // 10) % 10
    unidades = numero % 10

    # Cria strings para representar as partes do número
    centenas_str = ""
    dezenas_str = ""
    unidades_str = ""

    # Define os nomes das centenas, dezenas e unidades
    nomes_centenas = ["", "centena", "centenas"]
    nomes_dezenas = ["", "dezena", "dezenas"]
    nomes_unidades = ["", "unidade", "unidades"]

    # Formata as strings com os nomes das partes do número
    if centenas > 0:
        centenas_str = f"{centenas} {nomes_centenas[centenas if centenas != 1 else 2]}"
    if dezenas > 0:
        dezenas_str = f"{dezenas} {nomes_dezenas[dezenas if dezenas != 1 else 2]}"
    if unidades > 0:
        unidades_str = f"{unidades} {nomes_unidades[unidades if unidades != 1 else 2]}"

    # Monta a saída formatada
    saida = ", ".join(filter(None, [centenas_str, dezenas_str, unidades_str]))

    # Exibe o resultado
    print(saida)
