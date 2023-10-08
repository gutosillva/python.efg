#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
#Faça um programa capaz de gerar a série até o n−ésimo termo.

n = int(input("Digite o valor de n para gerar a série de Fibonacci: "))

a, b = 1, 1

if n <= 0:
    print("Por favor, insira um valor positivo para n.")
elif n == 1:
    print("Série de Fibonacci até o 1º termo:")
    print(a)
else:
    print("Série de Fibonacci até o", n, "º termo:")
    print(a, end=", ")
    print(b, end=", ")

    for _ in range(2, n):
        c = a + b
        print(c, end=", ")
        a, b = b, c

