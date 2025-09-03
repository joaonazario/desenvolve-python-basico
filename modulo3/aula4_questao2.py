'''
Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários.
Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5.
O programa deve imprimir uma mensagem correspondente à classificação do filme:

Se a avaliação for 5, imprima "Excelente!"
Se a avaliação for 4, imprima "Muito Bom!"
Se a avaliação for 3, imprima "Bom!"
Se a avaliação for 2, imprima "Regular."
Se a avaliação for 1, imprima "Ruim."
'''
# tomei a liberdade de avançar mais um pouco e usar ELIF
nota_filme = int(input("Digite uma nota de 0 a 5 para esse filme: "))

if nota_filme == 5:
    print(f"Excelente")
elif nota_filme == 4:
    print(f"Muito Bom!")
elif nota_filme == 3:
    print(f"Bom")
elif nota_filme == 2:
    print(f"Regular")
elif nota_filme == 1:
    print(f"Ruim")