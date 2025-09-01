"""
1 - Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura),
bem como o preço do metro quadrado da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado
como mostra o exemplo a seguir:
O terreno possui 250m2 e custa R$512,490.50
Comente na linha acima de cada instrução uma breve descrição da instrução.
Fórmulas:
area_m2 = comprimento * largura
preco_total = preco_m2 * area_m2
"""
#Cria e recebe os valores das variaveis necessarias
comprimentoTerreno = int(input("Digite o comprimento do terreno em metros: "))
larguraTerreno = int(input("Digite a largura do terreno em metros: "))
valorMetroQuadrado = float(input("Digite o valor do metro quadrado do terreno R$: "))

# Calcula a area em metros quadrados e o preço total do terreno 
area_m2 = comprimentoTerreno * larguraTerreno
preco_total = valorMetroQuadrado * area_m2

# Imprime as informaçoes do terreno
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f} reais")
