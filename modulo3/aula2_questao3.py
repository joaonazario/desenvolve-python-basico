'''
3 - Você está desenvolvendo um sistema de admissão para um clube juvenil de jogos de tabuleiro.
Escreva um programa em Python que pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos de tabuleiro
(resposta deve ser True ou False) e quantas vezes venceu um jogo. O programa deve imprimir True se o participante tiver entre 16 e 18 anos,
já tiver jogado pelo menos 3 jogos e já ter vencido pelo menos 1 jogo, permitindo seu ingresso no clube. Sua expressão deve
imprimir False caso contrário. Aqui está um exemplo de interação com seu código no terminal, com entradas de dados destacadas em
laranja e as impressões de seu código em branco.

Terminal:
Digite sua idade: 17
Já jogou pelo menos 3 jogos de tabuleiro? True
Quantos jogos já venceu? 2
Apto para ingressar no clube de jogos de tabuleiro: True
'''

idade_jogador = int(input("Digite a idade do jogador: "))
qnt_jogos = int(input("Quantos jogos o jogador participou? "))
venceu_jogos = int(input("Quantos jogos o jogador ja venceu? "))

qnt_permitida = qnt_jogos >= 3
qnt_vitorias = venceu_jogos >= 1
idade_permitida = idade_jogador >= 16 or idade_jogador <= 18
permissao_final = qnt_permitida and qnt_vitorias and idade_permitida

print(f"Ja jogou pelo menos 3 jogos de tabuleiro?{qnt_permitida}")
print(f"Quantos jogos já venceu? {venceu_jogos} {qnt_vitorias}")
print(f"Apto a ingressar no clube de jogos de tabuleiro: {permissao_final}")

