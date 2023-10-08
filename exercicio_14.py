#Faça um programa que lê as duas notas parciais obtidas por um aluno 
#numa disciplina ao longo de um semestre, e calcule a sua média. 
#A atribuição de conceitos obedece à tabela abaixo:
#Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
#e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
nota_1=int(input("Digite sua nota do primeiro semestre:"))
nota_2=int(input("Digite sua nota do segundo semestre:"))
nota_final=(nota_1+nota_2)/2 
if nota_final >= 9:
    print(f"primeiro semestre:{nota_1:.2f}")
    print(f"segundo semestre:{nota_2:.2f}")
    print(f"Sua media final:{nota_final:.2f}")
    print("Você tirou A")
    print("Você foi APROVADO")
elif nota_final >= 7.5 and nota_final < 9:
    print(f"primeiro semestre:{nota_1:.2f}")
    print(f"segundo semestre:{nota_2:.2f}")
    print(f"Sua media final:{nota_final:.2f}")
    print("Você tirou B")
    print("Você foi APROVADO")
elif nota_final >= 6 and nota_final < 7.5:
    print(f"primeiro semestre:{nota_1:.2f}")
    print(f"segundo semestre:{nota_2:.2f}")
    print(f"Sua media final:{nota_final:.2f}")
    print("Você tirou C")
    print("Você foi APROVADO")
elif nota_final >= 4 and nota_final < 6:
    print(f"primeiro semestre:{nota_1:.2f}")
    print(f"segundo semestre:{nota_2:.2f}")
    print(f"Sua media final:{nota_final:.2f}")
    print("Você tirou D")
    print("Você foi REPROVADO")
elif nota_final >= 0 and nota_final < 4:
    print(f"primeiro semestre:{nota_1:.2f}")
    print(f"segundo semestre:{nota_2:.2f}")
    print(f"Sua media final:{nota_final:.2f}")
    print("Você tirou E")
    print("Você foi REPROVADO")
    
nota_1 = float(input("Digite sua nota do primeiro semestre:"))
nota_2 = float(input("Digite sua nota do segundo semestre:"))
nota_final = (nota_1 + nota_2) / 2

if nota_final >= 9:
    conceito = "A"
    resultado = "APROVADO"
elif nota_final >= 7.5:
    conceito = "B"
    resultado = "APROVADO"
elif nota_final >= 6:
    conceito = "C"
    resultado = "APROVADO"
elif nota_final >= 4:
    conceito = "D"
    resultado = "REPROVADO"
else:
    conceito = "E"
    resultado = "REPROVADO"

print(f"Primeiro semestre: {nota_1:.2f}")
print(f"Segundo semestre: {nota_2:.2f}")
print(f"Sua média final: {nota_final:.2f}")
print(f"Você tirou {conceito}")
print(f"Você foi {resultado}")

