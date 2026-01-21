from random import shuffle

# Programa que sorteia a ordem de apresentação dos alunos
# A função shuffle embaralha a ordem dos elementos da lista

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

# Lista com os nomes dos alunos
alunos = [n1, n2, n3, n4]

# Embaralha a ordem da lista
shuffle(alunos)

# Exibe a ordem de apresentação
print('A ordem de apresentação será:')
print(alunos)
