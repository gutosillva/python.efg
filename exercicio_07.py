#Faça um programa que leia 5 números e informe o maior número.

# Inicialize uma variável para armazenar o maior número com um valor muito pequeno
maior_numero = float('-inf')

# Peça ao usuário para inserir 5 números
for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número: "))
    
    # Verifique se o número atual é maior que o maior número anterior
    if numero > maior_numero:
        maior_numero = numero

# Após o loop, imprima o maior número
print(f"O maior número é: {maior_numero}")