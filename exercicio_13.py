#Faça um Programa que leia um número e exiba o dia corresponde
#nte da semana. (1-Domingo, 2- Segunda, etc.), 
#se digitar outro valor deve aparecer valor inválido.
    semana=int(input("Digite um numero de 1 a 7:"))
    if semana == 1:
        print("Domingo é o primeiro dia da semana")
    elif semana == 2:
        print("Hoje é segunda-feira! Tem aula!")
    elif semana == 3:
        print("Hoje é Terça-feira!")
    elif semana == 4: 
        print("Hoje é Quarta-feira! Metade já foi")
    elif semana == 5:
        print("Hoje é Quinta-feira! UHUUU tá chegando já")
    elif semana == 6:
        print("EBAAAA Sexta-feira!!! Até que enfim a semana acabou")
    elif semana == 7:
        print("sabádo!!! Mas já")
    else:   
        print("valor invalido")