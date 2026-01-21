# Programa que lê o nome de uma cidade
# e verifica se ela começa com a palavra "Santo"

# strip() remove espaços extras no início e no fim
cidade = input('Digite uma cidade: ').strip()

# [:5] pega os 5 primeiros caracteres da string
# upper() transforma o texto em maiúsculas para evitar erro de comparação
# == 'SANTO' verifica se o início do nome é igual a "SANTO"
print(cidade[:5].upper() == 'SANTO')

