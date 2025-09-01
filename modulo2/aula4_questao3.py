'''
3 - Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online.
O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome,
o preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra. Note no exemplo a seguir que:
Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito)
A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de milhar e duas casas decimais).
Entrada
Saída
Digite o nome do produto 1:calça
Digite o preço unitário do produto 1:199.90
Digite a quantidade do produto 1: 3
Digite o nome do produto 2:camisa
Digite o preço unitário do produto 2:49.95
Digite a quantidade do produto 2:10
Digite o nome do produto 3:cinto
Digite o preço unitário do produto 3:25
Digite a quantidade do produto 3:3
Total: R$1,174.20
'''

nome_produto_01 = str(input("Digite o nome do produto 1: "))
preco_produto_01 = float(input("Digite o preço unitario do produto 1: "))
quant_produto_01 = int(input("Digite a quantas unidades desse produto você deseja: "))
total_produto_01 = quant_produto_01 * preco_produto_01

nome_produto_02 = str(input("Digite o nome do produto 2: "))
preco_produto_02 = float(input("Digite o peço do produto 2: "))
quant_produto_02 = int(input("Digite a quantas unidades desse produto você deseja: "))
total_produto_02 = quant_produto_02 * preco_produto_02

nome_produto_03 = str(input("Digite o nome do produto 3: "))
preco_produto_03 = float(input("Digite o peço do produto 3: "))
quant_produto_03 = int(input("Digite a quantas unidades desse produto você deseja: "))
total_produto_03 = quant_produto_03 * preco_produto_03

total_compra = total_produto_01 + total_produto_02 + total_produto_03
print(f"Valor total: R${total_compra} ")
