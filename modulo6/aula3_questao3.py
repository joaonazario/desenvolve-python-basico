'''
Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente.
Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del.
Você deve imprimir a lista antes e depois da deleção.
'''
import random

def main():
   
    lista_original = [random.randint(-10, 10) for _ in range(20)]
    print(f"Lista original: {lista_original}")
    
    
    maior_sequencia = 0
    posicao_inicial = -1
    
    
    sequencia_atual = 0
    posicao_atual = -1
    
    
    for i, numero in enumerate(lista_original):
        if numero < 0:
            sequencia_atual += 1
            if sequencia_atual == 1:
                posicao_atual = i
        else:
            if sequencia_atual > maior_sequencia:
                maior_sequencia = sequencia_atual
                posicao_inicial = posicao_atual
            sequencia_atual = 0

    
    if sequencia_atual > maior_sequencia:
        maior_sequencia = sequencia_atual
        posicao_inicial = posicao_atual
    
    
    if posicao_inicial != -1:
        del lista_original[posicao_inicial : posicao_inicial + maior_sequencia]

    print(f"Maior sequência de negativos: {maior_sequencia} elementos.")
    print(f"Lista editada: {lista_original}")

if __name__ == "__main__":
    main()