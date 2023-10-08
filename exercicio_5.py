#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.
bimestre1=int(input("Nota 1° Bimestre:"))
bimestre2=int(input("Nota 2° Bimestre:"))
bimestre3=int(input("Nota 3° Bimestre:"))
bimestre4=int(input("Nota 4° Bimestre:"))
media=bimestre1+bimestre2+bimestre3+bimestre4
media2=(media/4)
print("Sua media foi:", media2)
if media2==7:
    print("Quase que você não passa!!!")
if media2>7:
    print("Parabéns! Aprovado!") 
if media2==10:
    print("Na mosca!!!!")
if media2==6:
    print("Você quase conseguiu! Não desista agora!")
if media2<7:
    print("Que pena! Você foi reprovado!")
if media2<4:
    print("Poxa, passou longe hem!")