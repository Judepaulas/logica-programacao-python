# Programa que calcula o valor final de um produto
# após aplicar um desconto percentual

preco = float(input('Digite o valor do produto: R$ '))
desconto = float(input('Digite o percentual de desconto: '))

# Cálculo do valor com desconto
novo_preco = preco - (preco * desconto / 100)

# Exibe o resultado
print(
    'O valor do produto de R$ {:.2f} passará a ser R$ {:.2f}'.format(
        preco, novo_preco
    )
)
