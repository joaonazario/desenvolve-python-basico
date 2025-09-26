def calcular_digito_verificador(numeros, multiplicadores):
    soma = 0
    
    for num, mult in zip(numeros, multiplicadores):
        soma += num * mult
        
    resto = soma % 11
    
    if resto < 2:
        return 0
    else:
        return 11 - resto

def validar_cpf(cpf):
    cpf_limpo = cpf.replace('.', '').replace('-', '')
    
    if len(cpf_limpo) != 11:
        return "Inválido (Tamanho incorreto)"

    if cpf_limpo == cpf_limpo[0] * 11:
        return "Inválido (Sequência de dígitos iguais)"

    base_9_digitos = [int(d) for d in cpf_limpo[:9]]
    
    mult_d1 = list(range(10, 1, -1))
    
    primeiro_digito_calculado = calcular_digito_verificador(base_9_digitos, mult_d1)
    
    primeiro_digito_fornecido = int(cpf_limpo[9])
    
    if primeiro_digito_calculado != primeiro_digito_fornecido:
        return "Inválido (Primeiro dígito incorreto)"
    
    base_10_digitos = base_9_digitos + [primeiro_digito_calculado]
    
    mult_d2 = list(range(11, 1, -1))
    
    segundo_digito_calculado = calcular_digito_verificador(base_10_digitos, mult_d2)
    
    segundo_digito_fornecido = int(cpf_limpo[10])
    
    if segundo_digito_calculado != segundo_digito_fornecido:
        return "Inválido (Segundo dígito incorreto)"

    return "Válido"

cpf_entrada = input("Digite o CPF (XXX.XXX.XXX-XX): ")

cpf_entrada = cpf_entrada.strip() 

resultado = validar_cpf(cpf_entrada)
print(f"Status do CPF: {resultado}")