# Programa que lê o nome completo de uma pessoa
# e verifica se o nome contém a palavra "Silva"

nome = input('Digite seu nome completo: ')

# upper() padroniza o texto para maiúsculas
# in verifica se a palavra "SILVA" existe dentro da string
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
