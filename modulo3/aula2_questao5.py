'''
5 - Solicite de um usuário seu gênero ("M" ou "F"),
sua idade e seu tempo de serviço (em anos) e escreva uma expressão que imprima
True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:
A: Para mulheres, ter mais de 60 anos. Para homens, 65.
B: Ou ter trabalhado pelo menos 30 anos
C: Ou ter 60 anos  e trabalhado pelo menos 25.
'''
sexo_user = input("Digite o seu sexo (masculino ou feminino): ")
idade_user = int(input("Digite a sua idade (em anos): "))
tempo_user = int(input("Digite quanto tempo de serviço (em anos): "))

permissao_aposentar = (sexo_user =="feminino" and idade_user > 60) or (sexo_user == "masculino" and idade_user > 65) or (tempo_user >= 30) or (idade_user >= 60 and tempo_user >= 25)

print(permissao_aposentar)
