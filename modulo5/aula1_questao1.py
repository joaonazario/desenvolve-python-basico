"""
Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e calcule a
diferença absoluta entre esses dois números.
Utilize a função nativa abs para garantir que o resultado seja sempre positivo e round para arredondar
o resultado para duas casas decimais.
"""

n1 = float(input("Insira o primeiro numero decimal: "))
n2 = float(input("Insira o segundo numero decimal: "))

difs = abs(n1 - n2)
difs_round = round(difs, 2)

print(f"A diferença absoluta entre {n1} e {n2} é: {difs_round}")