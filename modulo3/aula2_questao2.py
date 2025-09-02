'''
2 - Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior de idade
(ficando responsável pelas outras).Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris,
mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False caso contrário.
'''

juliana = int(input("Digite e idade da Juliana: "))
cris = int(input("Digite a idade da Cris: "))

# processar informaçoes e saida
acesso_permitido = juliana > 17 or cris > 17

print(acesso_permitido)