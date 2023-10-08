#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, 
#mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser 
#informados também pelo usuário, conforme exemplo abaixo:
#Montar a tabuada de: 5
#Começar por: 4
#Terminar em: 7
#Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#5 X 4 = 20
#5 X 5 = 25
#5 X 6 = 30
#5 X 7 = 35
#Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

numero_usuario = int(input("Digite a tabuada que deseja reaizar: "))
numero_inicial = int(input("Digite o numero que a tabuada deve começar: "))
numero_final = int(input("Digite o numero que a tabuada deve terminar: "))

if numero_final < numero_inicial:
    print("O valor inicial da tabuada deve ser menor que o final")
    exit()
else:
    print(f"Vou montar a tabuada de {numero_usuario} começando em {numero_inicial} e terminando em {numero_final}:")
    for i in range(numero_inicial,numero_final + 1):
        resultado = numero_usuario * i
        print(f"{numero_usuario} X {i} = {resultado}")
    
    
    