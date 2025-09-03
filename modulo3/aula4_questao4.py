'''
Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote.
Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas.
O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
Distância até 100 km: R$1 por kg.
Distância entre 101 e 300 km: R$1.50 por kg.
Distância acima de 300 km: R$2 por kg.
Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg
'''
distancia = int(input("Digite a distancia em KM: "))
peso = int(input("Digite o peso da entrega: "))
taxa = 10
   
if distancia <= 100:
    valor_entrega = distancia * peso
elif distancia <= 100:
    valor_entrega = distancia * peso
elif distancia <= 100:
    valor_entrega = distancia * peso
elif distancia <= 100:
    valor_entrega = distancia * peso

if peso > 10:
    print(f"O valor bruto da entrega é: {valor_entrega}, houve o adicional de 10 reais devido ao peso da mercadoria, o Valor total é: {valor_entrega + 10}")
else: print(f"O valor da entrega é: {valor_entrega}")