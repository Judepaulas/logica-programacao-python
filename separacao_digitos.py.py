# Programa que lê um número de 0 a 9999
# e mostra seus dígitos separados

num = int(input('Informe um número: '))

# Unidade: divide por 1 e pega o resto da divisão por 10
u = num // 1 % 10

# Dezena: divide por 10 e pega o resto da divisão por 10
d = num // 10 % 10

# Centena: divide por 100 e pega o resto da divisão por 10
c = num // 100 % 10

# Milhar: divide por 1000 e pega o resto da divisão por 10
m = num // 1000 % 10

# Exibe os resultados
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
