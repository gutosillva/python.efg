#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
#O usuário deve informar de qual numero ele deseja ver a tabuada. 
#A saída deve ser conforme o exemplo abaixo:
#Tabuada de 5:
#5 X 1 = 5
#5 X 2 = 10
 
numero_usuario = int(input("Digite um numero inteiro de 1 a 10"))
print(f"Essa é a tabuada do {numero_usuario}:")
for i in range(1,11):
    resultado = i * numero_usuario
    print(f"{numero_usuario} X {i} = {resultado}")