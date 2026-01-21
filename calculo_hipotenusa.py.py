import math

# Programa que calcula a hipotenusa de um triângulo retângulo
# a partir do cateto oposto e do cateto adjacente

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))

# Cálculo da hipotenusa usando a função hypot da biblioteca math
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

# Exibe o resultado
print('A hipotenusa vai medir: {:.2f}'.format(hipotenusa))
