# Programa que lê o nome completo de uma pessoa
# e mostra o primeiro e o último nome

# strip() remove espaços extras no início e no fim
nome_completo = input('Digite seu nome completo: ').strip()

# split() divide o nome em partes e cria uma lista
nomes = nome_completo.split()

# Exibe o nome completo
print('Muito prazer, {}'.format(nome_completo))

# nomes[0] acessa o primeiro nome da lista
print('Seu primeiro nome é: {}'.format(nomes[0]))

# len(nomes) - 1 acessa a última posição da lista
print('Seu último nome é: {}'.format(nomes[len(nomes) - 1]))
