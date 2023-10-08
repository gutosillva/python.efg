#O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, 
#que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a
#tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, 
#conforme o exemplo abaixo:
#Preço do pão: R$ 0.18
#Panificadora Pão de Ontem - Tabela de preços
#1 - R$ 0.18
#2 - R$ 0.36
#...
#50 - R$ 9.00

quant_pao = int(input("Quantos pães o cliente comprou: "))
preco = 0
if quant_pao > 50:
    print("Quantidade limite exedida")
    exit()
else:
    if quant_pao < 1:
        print("Quantidade invalida")
    elif quant_pao == 1:
        print("Preço a pagar: R$ 0,18")
    else:
        for i in range(quant_pao):
            preco += 0.18
    print(f"Quantidade de itens coprados: {quant_pao}")
    print(f"Preço a pagar:R$ {round(preco,2)}")
    