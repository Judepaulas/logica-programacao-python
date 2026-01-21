# Programa que converte um valor em reais para dólares
# utilizando uma cotação fixa

reais = float(input('Qual valor você tem na carteira? R$ '))

# Cotação fixa do dólar
cotacao_dolar = 3.27

# Conversão de reais para dólares
dolar = reais / cotacao_dolar

# Exibe o resultado formatado
print(
    'Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(
        reais, dolar
    )
)
