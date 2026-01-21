# Programa que converte um valor em metros
# para centímetros e milímetros

metros = float(input('Digite um valor em metros: '))

# Conversões
centimetros = metros * 100
milimetros = metros * 1000

# Exibe os resultados
print(
    'O valor de {} metros em centímetros é {} e em milímetros é {}'.format(
        metros, centimetros, milimetros
    )
)
