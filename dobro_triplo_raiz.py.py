# Programa que lê um número
# e calcula o dobro, o triplo e a raiz quadrada

n = int(input('Digite um valor: '))

# Cálculos matemáticos
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

# Exibe os resultados
print(
    'O dobro de {} é {}, o triplo é {} e a raiz quadrada é {}'.format(
        n, dobro, triplo, raiz
    )
)
