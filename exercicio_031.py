#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de 
#conveniências. Faça um programa que implemente uma caixa registradora rudimentar. 
#O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
#Um valor zero deve ser informado pelo operador para indicar o final da compra. 
#O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, 
#para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, 
#para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
#Lojas Tabajara 
#Produto 1: R$ 2.20
#Produto 2: R$ 5.80
#Produto 3: R$ 0
#Total: R$ 9.00
#Dinheiro: R$ 20.00
#Troco: R$ 11.00

produto_numero = 0
total_compra = 0
total_produtos = 0
preco_produtos = []

while True:
    preco_produto = float(input(f'Produto {produto_numero + 1}: R$ '))
    if preco_produto == 0:
        break
    produto_numero += 1
    total_produtos += 1
    preco_produtos.append(preco_produto)  
total_compra = sum(preco_produtos)  
print(f"Total da compra: R$ {total_compra:.2f}")
dinheiro = float(input('Qual é o valor pago pelo cliente: '))
troco = dinheiro - total_compra
print("\nDetalhes da compra:")
for i in range(total_produtos):
    print(f"Produto {i + 1}: R$ {preco_produtos[i]:.2f}")
print(f"Dinheiro: R$ {dinheiro:.2f}")
print(f"Troco: R$ {troco:.2f}")