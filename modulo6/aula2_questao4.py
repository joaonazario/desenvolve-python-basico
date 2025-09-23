'''
Crie um programa em Python que receba duas listas de números do usuário,
podendo cada lista ter uma quantidade diferente de valores.
Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista.
Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.
'''

import random

lista_um = []
lista_dois = []
lista_comb = []



lista1_qnt = int(input('Quantos numeros você deseja adicionar a primeira lista?'))
lista2_qnt = int(input('Quantos numeros você deseja adicionar a segunda lista?'))

for i in range(lista1_qnt):
    n = int (input('Digite um numero a ser armazenado na primeira lista'))
    lista_um.append(n)

for i in range(lista2_qnt):
    n = int (input('Digite um numero a ser armazenado na segunda lista'))
    lista_dois.append(n)


tamanho_menor = min(len(lista_um), len(lista_dois))

for i in range(tamanho_menor):
    lista_comb.append(lista_um[i])
    lista_comb.append(lista_dois[i])

if len(lista_um) > len(lista_dois):
    lista_comb.extend(lista_um[tamanho_menor:])
else:
    lista_comb.extend(lista_dois[tamanho_menor:])

print(f'A primeira lista feita é: {lista_um}')
print(f'A segunda lista feita é: {lista_dois}')
print(f'A terceira lista cobinada é: {lista_comb} ')
