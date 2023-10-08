#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e 
#limitando o fatorial a números inteiros positivos e menores que 16.

while True:
    fatorial_usuario = int(input("Digite um número inteiro positivo (menor que 16): "))
    
    if fatorial_usuario < 0 or fatorial_usuario >= 16:
        print("Valor inválido. O número deve ser um inteiro positivo menor que 16.")
    else:
        if fatorial_usuario == 0:
            print("A fatorial de 0 é igual a 1.")
        else:
            fatorial = 1 
            for i in range(1, fatorial_usuario + 1):
                fatorial *= i
            print(f"{fatorial_usuario}! = {fatorial}")
    
    continuar = input("Deseja calcular outro fatorial? (S/N): ")
    if continuar.lower() != 's':
        break
