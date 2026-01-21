# Programa que lê um número inteiro
# e mostra seu antecessor e sucessor

n = int(input('Digite um valor: '))

# Calcula o antecessor e o sucessor
antecessor = n - 1
sucessor = n + 1

# Exibe os resultados
print(
    'O antecessor de {} é {} e o sucessor é {}'.format(
        n, antecessor, sucessor
    )
)
