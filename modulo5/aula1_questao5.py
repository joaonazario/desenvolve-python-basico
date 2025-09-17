'''
Você está trabalhando em um sistema de mensagens instantâneas, que deve permitir o uso de emojis nas conversas entre pessoas. Faça:
No terminal, instale a biblioteca emoji usando o gerenciador de pacotes pip
$ pip install emoji
Conheça a função emoji.emojize()
Seu programa deve apresentar para o usuário a lista de emojis disponíveis com o texto correspondente a cada emoji.
Em seguida, solicite uma frase codificada ao usuário e apresente ela decodificada com a visualização de emojis (emojizada).
A seguir um exemplo de interação, com uma lista de emojis sugeridos. Você pode consultar o texto que codifica outros emojis indo nessa página e passando o mouse por cima do emoji desejado. 
Emojis disponíveis:
❤️ - :red_heart:
👍 - :thumbs_up:
🤔 - :thinking_face:
🥳 - :partying_face:
Digite uma frase e ela será emojizada:
Olá mundo! :red_heart:
Frase emojizada:
Olá mundo! ❤️  
'''

import emoji

emojis_sugeridos = {
    ":red_heart:": "❤️",
    ":thumbs_up:": "👍",
    ":thinking_face:": "🤔",
    ":partying_face:": "🥳"
}

print("Emojis disponíveis:")
for texto, emoji_char in emojis_sugeridos.items():
    print(f"{emoji_char} - {texto}")

print("-" * 30)

frase_codificada = input("Digite uma frase e ela será emojizada: ")

frase_emojizada = emoji.emojize(frase_codificada)

print("\nFrase emojizada:")
print(frase_emojizada)
