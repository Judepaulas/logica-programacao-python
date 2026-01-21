# Programa que lê o nome completo de uma pessoa
# e realiza diferentes análises sobre ele

# strip() remove espaços extras no início e no fim do texto
nome = input('Digite seu nome completo: ').strip()

# Exibe o nome digitado
print(nome)

# upper() e lower() transformam o texto em maiúsculas e minúsculas
print(nome.upper())
print(nome.lower())

# replace() substitui os espaços por nada ('')
# len() conta a quantidade total de caracteres
total_letras = len(nome.replace(' ', ''))
print(total_letras)

# split() divide o texto em partes, separando pelos espaços
nome_dividido = nome.split()

# Obtém o primeiro nome (posição 0 da lista)
primeiro_nome = nome_dividido[0]

# Exibe o primeiro nome e a quantidade de letras
print(primeiro_nome)
print(len(primeiro_nome))
