'''
Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados,
bem como a chave da criptografia. Regras:
Chave de criptografia: gere um valor n aleatório entre 1 e 10
Substitua cada caracter c pelo caracter c + n.
Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)
'''
import random

def encrypt(nomes):

    key_n = random.randint(1, 10)
    
    encrypted_names = []
    
    MIN_CHAR_CODE = 33
    MAX_CHAR_CODE = 126
    RANGE_SIZE = MAX_CHAR_CODE - MIN_CHAR_CODE + 1 
    
    for name in nomes:
        encrypted_name = ""
        for char in name:
            char_code = ord(char)
            
            
            if MIN_CHAR_CODE <= char_code <= MAX_CHAR_CODE:
                
                
                original_pos = char_code - MIN_CHAR_CODE
                
                
                new_pos = (original_pos + key_n) % RANGE_SIZE
                
                new_code = new_pos + MIN_CHAR_CODE
                
                encrypted_name += chr(new_code)
            else:
                
                encrypted_name += char
                
        encrypted_names.append(encrypted_name)
        
    return encrypted_names, key_n

nomes = ["Jose", "Alejo", "Zara", "Michael"]

nomes_criptografados, chave = encrypt(nomes)

print(f"Nomes originais: {nomes}")
print(f"Chave de criptografia (n): {chave}")
print(f"Nomes criptografados: {nomes_criptografados}")