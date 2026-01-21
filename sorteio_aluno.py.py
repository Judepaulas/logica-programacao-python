from random import choice

# Programa que sorteia um nome a partir de uma lista de alunos
# A função choice escolhe aleatoriamente um elemento da lista

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

# Lista com os nomes dos alunos
alunos = [n1, n2, n3, n4]

# Sorteia um aluno aleatoriamente da lista
escolhido = choice(alunos)

# Exibe o resultado
print('O aluno escolhido foi {}'.format(escolhido))
