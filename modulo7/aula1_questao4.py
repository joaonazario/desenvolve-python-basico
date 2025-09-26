'''
Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente.
Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.
'''
number_cel = input(f'Digite o numero de cel: ')
if len(number_cel) == 8:
    number_cel = '9' + number_cel
    part_um = number_cel[:5]
    part_dois = number_cel[5:]
    number_cel = part_um + '-' + part_dois
elif len(number_cel) == 9 and number_cel[0] == '9':
    part_um = number_cel[:5]
    part_dois = number_cel[5:]
    number_cel = part_um + '-' + part_dois


print(f'Numero completo: {number_cel}')