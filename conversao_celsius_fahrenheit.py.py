# Programa que converte temperatura de Celsius para Fahrenheit

celsius = float(input('Informe a temperatura em °C: '))

# Fórmula de conversão de Celsius para Fahrenheit
# Multiplica por 9, divide por 5 e soma 32 conforme a fórmula padrão
fahrenheit = (9 * celsius / 5) + 32

# Exibe o resultado
print(
    'A temperatura de {:.2f} °C corresponde a {:.2f} °F!'.format(
        celsius, fahrenheit
    )
)
