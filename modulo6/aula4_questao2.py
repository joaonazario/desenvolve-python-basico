'''
Solicite uma frase do usuário e usando compreensão de listas imprima:
A lista de vogais da frase, ordenada alfabeticamente
A lista de consoantes da frase (remova espaços em branco)
'''
frase = input("Digite uma frase: ")

vogais = ['a', 'e', 'i', 'o', 'u']

lista_vogais = [char.lower() for char in frase if char.lower() in vogais]
lista_vogais.sort()

lista_consoantes = [char for char in frase if char.lower() not in vogais and char != ' ']

print(f"Vogais: {lista_vogais}")
print(f"Consoantes: {lista_consoantes}")
