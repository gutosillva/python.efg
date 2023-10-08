#Faça um Programa que peça um número correspondente a um determinado ano e 
#em seguida informe se este ano é ou não bissexto.
# Solicita ao usuário que digite um ano
ano = int(input("Digite um ano: "))

# Verifica se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
