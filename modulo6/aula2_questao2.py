'''
Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos.
Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos,
e armazene em uma lista chamada elementos.
Em seguida imprima:
A lista elementos
A soma dos valores da lista
A média dos valores da lista
'''

import random

num_elementos = random.randint(4,19)

elementos = []


for i in range (num_elementos):
    n = random.randint(0, 9)
    elementos.append(n)
    
soma_dos_numeros = sum(elementos)
quantidade = len(elementos)
media_dos_elementos = soma_dos_numeros / quantidade

print(f'O valor gerado foi: {num_elementos}')
print(f'Os numeros gerados foram {elementos}')
print(f'A soma dos elementos é: {soma_dos_numeros}')
print (f'A media da soma desses elementos é: {media_dos_elementos}')