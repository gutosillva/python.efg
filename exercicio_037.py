#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, 
#a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes 
#da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o 
#usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os 
#códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das 
#alturas e dos pesos dos clientes

menor_peso = float('inf') 
maior_peso = float('-inf')  
menor_altura = float('inf')
maior_altura = float('-inf')
soma_peso = 0
soma_altura = 0
contador_peso = 0
contador_altura = 0

while True:
    try:
        peso = float(input("Digite o peso do clientes: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue
    if peso == 0:
        break
    try:
        altura = float(input("Digite a altura do clientes: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue
    if altura == 0:
        break
    menor_peso = min(menor_peso, peso)
    maior_peso = max(maior_peso, peso)
    soma_peso += peso
    contador_peso += 1
    menor_altura = min(menor_altura, altura)
    maior_altura = max(maior_altura, altura)
    soma_altura += altura
    contador_altura += 1
media_peso = soma_peso / contador_peso if contador_peso > 0 else 0
media_altura = soma_altura / contador_altura if contador_altura > 0 else 0
  
print(f"Mais magro:{menor_peso} Kg")
print(f"Mais gordo:{maior_peso} Kg")
print(f"Mais baixo:{menor_altura} Cm")
print(f"Mais alto:{maior_altura} Cm")
print(soma_peso)
print(soma_altura)
print(f"A media do peso é:{round(media_peso,2)} Kg")
print(f"A media da altura é:{round(media_altura,2)} Cm")