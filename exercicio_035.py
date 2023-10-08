#Encontrar números primos é uma tarefa difícil. Faça um programa 
#que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
numero_limite = int(input("Digite um número inteiro: "))
numeros_primos = []
for num in range(2, numero_limite + 1):
    if eh_primo(num):
        numeros_primos.append(num)
print(f"Números primos entre 1 e {numero_limite}:")
print(numeros_primos)