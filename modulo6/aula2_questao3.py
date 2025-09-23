'''
Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50.
Crie uma terceira lista interseccao contendo apenas os valores que se repetem nas duas listas.
Ao final imprima:
Ambas as listas
A lista intersecção ordenada
A quantidade de vezes que cada elemento aparece em cada lista
'''
import random

num_elementos = 20
lista_um = []
lista_dois = []

for i in range (num_elementos):
    n_1 = random.randint(0,49)
    n_2 = random.randint(0,49)
    lista_um.append(n_1)
    lista_dois.append(n_2)

conj_um = set(lista_um)
conj_dois = set(lista_dois)
intersect = conj_um.intersection(conj_dois)
intersectlist = list(intersect)

print(f'Essa é a lista 1 {lista_um}')
print(f'Essa é a lista 2 {lista_dois}')
print(f'Essa é a intersseção entre as listas {intersect}')
print(f'Existem {len(intersect)} intersseçoes dentro da lista')