'''
4 - Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade
possível de notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1.
A saída deve estar formatada exatamente como indicado.
Entrada
Saída
576
5 nota(s) de R$100,00
1 nota(s) de R$50,00
1 nota(s) de R$20,00
0 nota(s) de R$10,00
1 nota(s) de R$5,00
0 nota(s) de R$2,00
1 nota(s) de R$1,00
'''

# Recebe o valor inteiro da quantia
valor = int(input("Digite o valor a pagar: R$"))

# Exibe o valor total
print(valor)

# Calcula o número de notas de R$100,00
notas_100 = valor // 100
valor = valor % 100
print(f"{notas_100} nota(s) de R$100,00")

# Calcula o número de notas de R$50,00
notas_50 = valor // 50
valor = valor % 50
print(f"{notas_50} nota(s) de R$50,00")

# Calcula o número de notas de R$20,00
notas_20 = valor // 20
valor = valor % 20
print(f"{notas_20} nota(s) de R$20,00")

# Calcula o número de notas de R$10,00
notas_10 = valor // 10
valor = valor % 10
print(f"{notas_10} nota(s) de R$10,00")

# Calcula o número de notas de R$5,00
notas_5 = valor // 5
valor = valor % 5
print(f"{notas_5} nota(s) de R$5,00")

# Calcula o número de notas de R$2,00
notas_2 = valor // 2
valor = valor % 2
print(f"{notas_2} nota(s) de R$2,00")

# Calcula o número de notas de R$1,00
notas_1 = valor // 1
valor = valor % 1
print(f"{notas_1} nota(s) de R$1,00")