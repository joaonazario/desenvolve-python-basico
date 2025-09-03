'''
Você está desenvolvendo um programa para verificar se um ano é bissexto.
Escreva um código em Python que solicita ao usuário para inserir um ano e imprime
"Bissexto" se o ano for (1) divisível por 4 e não for divisível por 100, ou (2) se for divisível por 400.
Caso contrário, imprima "Não Bissexto". 

Teste seu código com os valores: 1900 (não bissexto), 2000 (bissexto), 2016 (bissexto) e 2017 (não bissexto). 
'''

ano_bisexto = int(input("Digite o ano que você deseja consultar"))

if (ano_bisexto % 4 == 0 and ano_bisexto % 100 != 0) or (ano_bisexto % 400 == 0):
    print(f"Bisexto")
else:
    print(f"Não Bissexto")