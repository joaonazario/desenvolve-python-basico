'''
3.Transforme em código o fluxograma a seguir
'''
n1 = int(input("Digite o valor de N1: "))
n2 = int(input("Digite o valor de N2: "))
n3 = int(input("Digite o valor de N3: "))

m = (n1 + n2 + n3) / 3

if m >= 60:
    print(f"Aprovado")

elif m >= 40 and m< 60 :
    print(f"Recuperação")
    
else:
    print(f"Reprovado")

print(f"FIM")
