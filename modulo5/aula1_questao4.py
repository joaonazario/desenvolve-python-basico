'''
Escreva um programa em Python que utiliza a biblioteca datetime para exibir a data e hora atuais com a formatação apresentada a seguir:

Data: 15/03/2023 

Hora: 14:05
'''
from datetime import datetime

agora = datetime.now()
print(f"Agora sem formatar é: {agora}")
hora_format = agora.strftime("%H:%M:%S %d:%m:%Y")
print(f"A hora atual é formatada é: {hora_format}")



