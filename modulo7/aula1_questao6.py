'''
Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo.
Anagramas são palavras com os mesmos caracteres rearranjados.
'''
frase = input(f'Digite a frase')
palavra_busca = input('Digite a palavra')
anagramas = []
palavras_chave = sorted(palavra_busca)

for palavra in frase.split():
    chave_palavra = sorted(palavra)
    if chave_palavra == palavras_chave:
        anagramas.append(palavra)

print(anagramas)