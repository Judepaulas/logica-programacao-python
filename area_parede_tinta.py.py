# Programa que calcula a área de uma parede
# e a quantidade de tinta necessária para pintá-la

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

# Cálculo da área da parede
area = largura * altura

# Considerando que 1 litro de tinta pinta 2 m²
tinta = area / 2

# Exibe os resultados
print(
    'A parede tem {:.2f} x {:.2f} e a área é de {:.2f} m²'.format(
        largura, altura, area
    )
)

print(
    'Para pintar a parede, você precisará de {:.2f} litros de tinta.'.format(
        tinta
    )
)
