'''
Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista.
Em seguida imprima na ordem estabelecida:
A lista ordenada, sem modificar a lista original
A lista original
O índice do maior valor da lista
O índice do menor valor da lista
'''

import random

lista = []
for i in range(0, 20):
    n = random.randint(-100, 100)
    lista.append(n)

print(f"Lista ordenada: {sorted(lista)}")
print(f"Lista original: {lista}")
print(f"Maior valor da lista: {max(lista)}")
print(f"Maior valor da lista: {min(lista)}")
