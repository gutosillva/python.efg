import random

# Lista de possíveis respostas
respostas = ["sim", "não"]

while True:
    pergunta = input("Faça uma pergunta (ou digite 'sair' para encerrar): ").strip().lower()

    if pergunta == 'sair':
        print("Programa encerrado.")
        break

    resposta = random.choice(respostas)
    print("Resposta:", resposta)
