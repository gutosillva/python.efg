#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
# Solicita ao usuário que digite uma letra
letra = input("Digite uma letra (F para Feminino, M para Masculino): ")

# Converte a letra para maiúscula para garantir a comparação correta
letra = letra.upper()

# Verifica se a letra é "F" ou "M" e exibe a mensagem correspondente
if letra == "F":
    print("F - Feminino")
elif letra == "M":
    print("M - Masculino")
else:
    print("Sexo Inválido")
