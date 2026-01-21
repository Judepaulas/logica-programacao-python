# Programa que recebe um valor do usuário
# e verifica suas características usando métodos de string

a = input('Digite algo: ')

# Mostra o tipo primitivo do valor digitado
print('O tipo primitivo desse valor é:', type(a))

# Verifica se o valor contém apenas espaços
print('Só tem espaços?', a.isspace())

# Verifica se o valor é numérico
print('É um número?', a.isnumeric())

# Verifica se o valor contém apenas letras
print('É alfabético?', a.isalpha())

# Verifica se o valor é alfanumérico (letras e números)
print('É alfanumérico?', a.isalnum())

# Verifica se está em letras maiúsculas
print('Está em maiúsculas?', a.isupper())

# Verifica se está em letras minúsculas
print('Está em minúsculas?', a.islower())

# Verifica se a primeira letra de cada palavra é maiúscula
print('Está capitalizada?', a.istitle())

