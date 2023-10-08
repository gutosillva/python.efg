#Faça um programa que calcule o número médio de alunos por turma. 
#Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
#As turmas não podem ter mais de 40 alunos.

sala = int(input("Quantas salas de aula tem na sua escola: "))
media = 0
for i in range (sala):
    aluno = int(input(f"Digite a quantidade de alunos da {i+1}ª sala"))
    if aluno > 40:
        print("A quantidade de alunos não pode ultrapassar 40")
        exit()
    else:
        media += aluno
media_final = round(media / sala)
print(f"A media de alunos dessa escola é de: {media_final} alunos em cada sala")