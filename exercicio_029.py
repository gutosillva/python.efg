#O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. 
#Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número 
#de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa 
#apenas contar quantos itens o cliente está levando e olhar na tabela de preços. 
#Você foi contratado para desenvolver o programa que monta esta tabela de preços, 
#que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
#Lojas Quase Dois - Tabela de preços
#1 - R$ 1.99
#2 - R$ 3.98
#...
#50 - R$ 99.50
while True:
    quant_itens_comprados = int(input("Quantos produtos o cliente comprou: "))
    preco = 0
    if quant_itens_comprados > 50:
        print("Quantidade limite excedida")
        exit()
        if quant_itens_comprados < 1:
            print("Quantidade invalida")
        elif quant_itens_comprados == 1:
            print("Preço a pagar: R$1,99")
        else:
            for i in range(quant_itens_comprados):
                preco += 1.99
        print(f"Quantidade de itens coprados: {quant_itens_comprados}")
        print(f"Preço a pagar:R${round(preco,2)}")
        continuar = input("Deseja calcular outro fatorial? (S/N): ")
        if continuar.lower() != 's':
            break