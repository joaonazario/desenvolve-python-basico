'''
4. Transforme em código o fluxograma a seguir
'''
n = int(input("Digite o valor de N: "))
maior = 0
while n > 0:
    x = int(input("Digite o valor de X:"))
    if x > maior:
        maior = x
    n = n - 1
print(f"Maior{maior}")