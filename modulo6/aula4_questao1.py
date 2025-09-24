'''
Escreva um script python que use compreensão de listas para criar as seguintes listas:
Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
Todos os números entre 1 e 100 que sejam divisíveis por 7
Para todos os valores em range(0,30,3), escreva "par" ou "ímpar"
dependendo da paridade do elemento (ex:['par', 'impar',… , 'impar']) 
'''

pares_entre_20_e_50 = [numero for numero in range(20, 51) if numero % 2 == 0]
print(f"Pares entre 20 e 50: {pares_entre_20_e_50}")

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrados = [valor**2 for valor in valores]
print(f"Quadrados dos valores: {quadrados}")

divisiveis_por_7 = [numero for numero in range(1, 101) if numero % 7 == 0]
print(f"Divisíveis por 7 entre 1 e 100: {divisiveis_por_7}")


paridade_range = ["par" if numero % 2 == 0 else "ímpar" for numero in range(0, 30, 3)]
print(f"Paridade dos elementos: {paridade_range}")
