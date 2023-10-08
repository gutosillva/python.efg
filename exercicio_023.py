#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
#O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
#Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

def eh_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def listar_primos_ate_n(N):
    primos = []
    divisoes = 0
    for numero in range(2, N + 1):
        divisoes += 1
        if eh_primo(numero):
            primos.append(numero)
    return primos, divisoes

N = int(input("Digite um número inteiro N: "))
primos, divisoes = listar_primos_ate_n(N)

print("Números primos entre 1 e", N, "são:", primos)
print("Número total de divisões executadas:", divisoes)
