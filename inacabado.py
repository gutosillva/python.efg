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
preco_produto = []
while True:
    preco_produto = float(input(f'Produto {produto_numero + 1}: R$ '))
    produto_numero += 1
    total_produtos += 1
    if preco_produto == 0:
        break
    total_compra += preco_produto
print(total_compra)
dinheiro = int(input('Qual é o valor pago pelo cliente: '))
troco = dinheiro - total_compra
for i in range(total_produtos):
    print(f"Produto {i + 1}: R$ {preco_produto[i]:.2f}")
print(f"Dinheiro: R$ {dinheiro}")
print(f"Troco: R${troco}")