# Programa que calcula o valor do aluguel de um carro
# considerando a quantidade de dias e os quilômetros percorridos

km = float(input('Qual a quantidade de km percorridos? '))
dias = int(input('Quantidade de dias alugados? '))

# Valores fixos
valor_diaria = 60.00
valor_km = 0.15

# Cálculo do valor total
total_pagar = (dias * valor_diaria) + (km * valor_km)

# Exibe o resultado
print(
    'O total a se pagar é de R$ {:.2f}'.format(
        total_pagar
    )
)
