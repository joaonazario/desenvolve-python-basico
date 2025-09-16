'''
Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule a raíz quadrada da soma dos valores.
Peça ao usuário o valor de n
Biblioteca random: Função randint()
Biblioteca math:  Função sqrt()
'''
import math
import random

n = int(input("Digite quantos numeros aleatorios você deseja gerar: "))
soma = 0
for i in range (n):
    num_random = random.randint (0, 100)
    print (num_random)
    soma += num_random


print(f"Essa é a soma dos numeros aleatorios: {soma}")
raiz = math.sqrt(soma)
print(f"Essa é a raiz quadrada da soma dos numeros {raiz}")