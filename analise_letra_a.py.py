# Programa que lê uma frase e analisa a letra "A"

# upper() transforma tudo em maiúsculas
# strip() remove espaços extras no início e no fim
frase = input('Digite uma frase: ').upper().strip()

# count() conta quantas vezes a letra "A" aparece na frase
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))

# find() mostra a posição da primeira ocorrência da letra "A"
# +1 ajusta a contagem para começar em 1
print('Ela aparece a primeira vez na posição {}.'.format(frase.find('A') + 1))

# rfind() mostra a posição da última ocorrência da letra "A"
# +1 ajusta a contagem para começar em 1
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A') + 1))
