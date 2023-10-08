#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre 
#a participação da pessoa no crime. Se a pessoa responder 
#positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e
#5 como "Assassino". 
#Caso contrário, ele será classificado como "Inocente".

# Inicialize um contador para armazenar o número de respostas positivas
contador_respostas_positivas = 0

# Faça as perguntas
resposta1 = input("Telefonou para a vítima? (Sim ou Não): ")
resposta2 = input("Esteve no local do crime? (Sim ou Não): ")
resposta3 = input("Mora perto da vítima? (Sim ou Não): ")
resposta4 = input("Devia para a vítima? (Sim ou Não): ")
resposta5 = input("Já trabalhou com a vítima? (Sim ou Não): ")

# Verifique as respostas e atualize o contador
if resposta1.lower() == "sim":
    contador_respostas_positivas += 1
if resposta2.lower() == "sim":
    contador_respostas_positivas += 1
if resposta3.lower() == "sim":
    contador_respostas_positivas += 1
if resposta4.lower() == "sim":
    contador_respostas_positivas += 1
if resposta5.lower() == "sim":
    contador_respostas_positivas += 1
    

# Emita a classificação com base no contador
if contador_respostas_positivas == 2:
    print("Você é Suspeito(a)!")
elif contador_respostas_positivas >= 3 and contador_respostas_positivas <= 4:
    print("Você é Cúmplice!")
elif contador_respostas_positivas == 5:
    print("Você é o Assassino!")
else:
    print("Você é Inocente!")
