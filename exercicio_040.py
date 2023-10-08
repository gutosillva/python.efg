#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
#Foram obtidos os seguintes dados:
#Código da cidade;
#Número de veículos de passeio (em 1999);
#Número de acidentes de trânsito com vítimas (em 1999). 
#Deseja-se saber:
#Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#Qual a média de veículos nas cinco cidades juntas;
#Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.


cidades = []
for i in range(5):
    codigo = int(input(f"Informe o código da cidade {i+1}: "))
    veiculos = int(input(f"Informe o número de veículos de passeio em 1999 na cidade {i+1}: "))
    acidentes = int(input(f"Informe o número de acidentes de trânsito com vítimas em 1999 na cidade {i+1}: "))
    
    cidade = {"codigo": codigo, "veiculos": veiculos, "acidentes": acidentes}
    cidades.append(cidade)

maior_acidentes = max(cidades, key=lambda x: x["acidentes"])
menor_acidentes = min(cidades, key=lambda x: x["acidentes"])

total_veiculos = sum([cidade["veiculos"] for cidade in cidades])
media_veiculos = total_veiculos / len(cidades)

cidades_menos_2000 = [cidade for cidade in cidades if cidade["veiculos"] < 2000]
total_acidentes_menos_2000 = sum([cidade["acidentes"] for cidade in cidades_menos_2000])
media_acidentes_menos_2000 = total_acidentes_menos_2000 / len(cidades_menos_2000)

print(f"Maior índice de acidentes: {maior_acidentes['acidentes']} na cidade {maior_acidentes['codigo']}")
print(f"Menor índice de acidentes: {menor_acidentes['acidentes']} na cidade {menor_acidentes['codigo']}")
print(f"Média de veículos nas cinco cidades: {media_veiculos}")
print(f"Média de acidentes de trânsito nas cidades com menos de 2.000 veículos: {media_acidentes_menos_2000}")
