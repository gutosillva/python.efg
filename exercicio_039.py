#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do
#aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. 
#Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

numero_aluno_mais_alto = 0
altura_aluno_mais_alto = 0
numero_aluno_mais_baixo = 0
altura_aluno_mais_baixo = float('inf')  
for i in range(1, 11):
    numero_aluno = int(input(f"Digite o número do {i}º aluno: "))
    altura_aluno = float(input(f"Digite a altura do {i}º aluno em centímetros: "))
    if altura_aluno > altura_aluno_mais_alto:
        numero_aluno_mais_alto = numero_aluno
        altura_aluno_mais_alto = altura_aluno
    if altura_aluno < altura_aluno_mais_baixo:
        numero_aluno_mais_baixo = numero_aluno
        altura_aluno_mais_baixo = altura_aluno
print(f"O aluno mais alto é o número {numero_aluno_mais_alto}, com {altura_aluno_mais_alto} cm de altura.")
print(f"O aluno mais baixo é o número {numero_aluno_mais_baixo}, com {altura_aluno_mais_baixo} cm de altura.")
