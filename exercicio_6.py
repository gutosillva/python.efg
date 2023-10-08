#Faça um Programa que leia três números e mostre o maior deles.
n1=int(input("Digite 1° numero:"))
n2=int(input("Digite 2° numero:"))
n3=int(input("Digite 3° numero:"))
if n1 > n2 and n1 > n3:
    print("O numero", n1,"é o maior")
if n2 > n1 and n2 > n3:
    print("O numero", n2,"é o maior")
if n3 > n2 and n3 > n1:
    print("O numero", n3,"é o maior")