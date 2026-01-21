# Radar eletrônico
# Programa que lê a velocidade de um carro
# Se ultrapassar 80 km/h, exibe uma mensagem de multa
# A multa custa R$7,00 para cada km acima do limite

velocidade = float(input('Qual a velocidade atual do carro? '))

# Verifica se a velocidade está acima do limite permitido
if velocidade > 80:
    print('MULTADO!!!')

    # Calcula a multa:
    # (velocidade - 80) representa apenas o valor excedente
    # Multiplicamos por 7 para obter o valor da multa
    multa = (velocidade - 80) * 7

    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    # Caso esteja dentro do limite permitido
    print('Tenha um bom dia, dirija com segurança!')

