'''
Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (com pelo menos 4 valores),
os armazena em uma lista e, usando fatiamento de listas, imprima:
A lista original
Os 3 primeiros elementos
Os 2 últimos elementos
A lista invertida (do fim para o começo)
Os elementos de índice par (0, 2, 4 … )
Os elementos de índice ímpar (1, 3, 5, … )
'''

n_inteiro = []

while len(n_inteiro) < 6:
    
        entrada = int(input('Digite um numero a ser adicionado a lista'))
        n_inteiro.append(entrada)
        

print(f'Exibindo Lista original: {n_inteiro}')
print(f'Exibindo os 3 primeiros elementos: {n_inteiro[:3]}')
print(f'Exibindo os 2 ultimos elementos: {n_inteiro[-2:]}')
print(f"Elementos de índice par: {n_inteiro[1::2]}")
print(f"Elementos de índice ímpar: {n_inteiro[::2]}")
