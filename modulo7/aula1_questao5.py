'''
Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string.
Dica: letra in "aeiou".
'''
frase = input('Digite uma frase: ').lower()
vogais = ['a','e','i','o','u']
indice = []
comparac = []
for i, char in enumerate (frase):
    if char in vogais:
        comparac.append(char) 
        indice.append(i)
        
print (f'Existem {len(comparac)} vogais na frase e elas são {comparac}')
print(f'Os indices das vogais na frase são: {indice}')