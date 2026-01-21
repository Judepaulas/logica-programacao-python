# Programa que calcula o novo salário de um funcionário
# após aplicar um aumento percentual

salario = float(input('Qual o valor do salário? R$ '))
aumento = float(input('Qual o percentual de aumento? '))

# Cálculo do novo salário com aumento
novo_salario = salario + (salario * aumento / 100)

# Exibe o resultado
print(
    'O salário de R$ {:.2f} passará a ser R$ {:.2f}'.format(
        salario, novo_salario
    )
)
