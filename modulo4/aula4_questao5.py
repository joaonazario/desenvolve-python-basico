'''
Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes.
Escreva um programa que leia um inteiro N com a quantidade de respondentes e em seguida leia as N idades de cada respondente.
Ao final, imprima a média das idades.

(idade1 + idade2 + idade3 + … + idade_n)/N
'''

n = int(input("Digite o numero de respondentes a pesquisa: "))
soma_idades = 0

while n > 0:
    idade = int(input("Digite a idade da pessoa: "))
    soma_idades += idade
    n -= 1

if n == 0:
    media = soma_idades / (n - soma_idades + soma_idades + 1)
else:
    print("Não é possível calcular a média com 0 respondentes.")
    
print(f"a média é: {media}")
