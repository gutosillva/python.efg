#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um 
#conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, 
#bem como a média das temperaturas.

menor_temp = float('inf')
maior_temp = float('-inf')  
soma_temps = 0
contador_temps = 0
while True:
    try:
        temperatura = float(input("Digite as temperaturas (ou 0 para sair):"))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue
    if temperatura == 0:
        break
    menor_temp = min(menor_temp, temperatura)
    maior_temp = max(maior_temp, temperatura)
    soma_temps += temperatura
    contador_temps += 1
    
if contador_temps > 0:
    media_temps = soma_temps / contador_temps
    print(f"A menor temperatura: {menor_temp}°C")
    print(f"A maior temperatura: {maior_temp}°C")
    print(f"A média das temperaturas: {media_temps:.2f}°C")
else:
    print("Nenhuma temperatura foi informada.")
        

    