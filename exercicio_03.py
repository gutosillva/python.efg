#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input("NOME: ")
while len(nome) < 3:
    print("String deve ter mais de três caracteres!")
    nome = input("NOME: ")
    
idade = int(input("IDADE: "))
while idade < 0 or idade > 150:
    print("Idade invalida")
    idade = int(input("IDADE: "))
    
salario = int(input("SALARIO: "))
while salario < 0:
    print("Salário tem que ser maior que 0!")
    salario = input("SALARIO: ")
    
sexo = input("SEXO: ")
sexo = sexo.lower()
while sexo != 'f' and sexo != 'm':
    print("Sexo inválido")
    sexo = input("SEXO: ")
    sexo = sexo.lower()

estado_civil = input("ESTADO CIVIL: ")
estado_civil = estado_civil.lower()

while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    print("Estado civil inválido")
    estado_civil = input("ESTADO CIVIL: ")
    estado_civil = estado_civil.lower()

print("Seus dados informados são:")
print("NOME:", nome)
print("IDADE:", idade)
print("SALARIO:", salario)
if sexo == 'm':
    print("SEXO: Masculino")
else:
    print("SEXO: Feminino" )
if estado_civil == 's':
    print("ESTADO CIVIL: Solteiro (a) ")
if estado_civil == 'c':
    print("ESTADO CIVIL: Casado (a)")
if estado_civil == '':
    print("ESTADO CIVIL: Viuvo (a)")
if estado_civil == 'd':
    print("ESTADO CIVIL: Divorciado (a)")


