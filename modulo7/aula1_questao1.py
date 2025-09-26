'''
Escreva um programa que solicita o nome do usuário e o imprime em forma de escada,
como indicado no exemplo a seguir.
'''
print(f'Vamos imprimir o seu nome em formato escada letra a letra:')
nome = input('Digite o seu nome: ')
for i in range (len(nome)):
    print(nome[:i+1])
