#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
#Faça um programa que gere a série até que o valor seja maior que 500.

fibonacci = [0, 1]

while fibonacci[-1] <= 500:
    next_number = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_number)

print(f"Série de Fibonacci até que o valor seja maior que 500: {fibonacci}")