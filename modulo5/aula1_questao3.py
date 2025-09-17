'''
Escreva um programa em Python que utiliza a biblioteca random para gerar um número
aleatório entre 1 e 10 e peça ao usuário para adivinhar o número. Forneça feedback se o palpite é muito alto,
muito baixo ou correto. Interrompa a execução somente quando o usuário acertar o palpite.
'''
import random

aleatorio = random.randint (1, 10)
n = 0
while n != aleatorio:
    n = int(input("Digite um numero para ser adivinhado de 0 a 10: - "))
    if n < aleatorio:
        print(f"Muito baixo tente novamente")   
    elif n > aleatorio:
        print(f"Muito alto, tente novamente")     
    if n == aleatorio:
        print(f"Correto o numero é {n}") 
    else:
        print(f"Digite um numero valido entre 0 e 10")
