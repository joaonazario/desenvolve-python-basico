'''
1 - Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17).
Escreva um programa que solicite as idades de Juliana e Cris e imprima True se ambas forem maiores de 17 anos,
indicando que podem entrar no bar, e False caso contrário.
'''

juliana = int(input("Digite e idade da Juliana"))
cris = int(input("Digite a idade da Cris"))

# processar informaçoes e saida
acesso_permitido = juliana > 17 and cris > 17

print(acesso_permitido)
