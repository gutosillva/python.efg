#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
#Valide a entrada e permita repetir a operação.

pais_a = int(input("Informe a população inicial do pais A: "))
taxa_usuario_a = int(input("Informe a taxa de crescimento anual em porcentagem: "))
taxa_a = taxa_usuario_a / 100

pais_b = int(input("Informe a população inicial do pais B: "))
taxa_usuario_b = int(input("Informe a taxa de crescimento anual: "))
taxa_b = taxa_usuario_b / 100

anos = 0 

while pais_a < pais_b:
    pais_a += pais_a * taxa_a
    pais_b += pais_b * taxa_b
    
    anos += 1
print(f"O pais A levará {anos} anos para ultrapassar ou igualar com pais B")