# Programa que mostra uma contagem usando for e range
# e informa quantos números foram exibidos

inicio = int(input("Digite o inicio da contagem: "))
fim = int(input("Digite o fim da contagem: "))

contador = 0 #Conta quantos números serão exibidos

for i in range(inicio,fim + 1):
    print(i)
    contador = contador + 1 #A cada número exibido soma 1
print("Foram exibidos {}, números ao todo" .format (contador))
