from random import randint

# Programa em que o computador escolhe um número
# e o usuário tenta adivinhar

# Gera um número aleatório entre 0 e 5
numero_computador = randint(0, 5)

# Exibe o layout do jogo
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-' * 20)

# Lê o palpite do jogador
jogador = int(input('Em que número eu pensei? '))

# Verifica se o jogador acertou
if jogador == numero_computador:
    print('VOCÊ VENCEU!!!')
else:
    print('EU GANHEI!!! Pensei no número {}'.format(numero_computador))
