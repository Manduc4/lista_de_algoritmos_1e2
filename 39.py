maior = float(0)
menor = float(1000)
for i in range (1,16):
    h = float(input('Altura {}:'.format(i)))
    if h > maior:
        maior = h
    if h < menor:
        menor = h
print('Maior altura: {}m'.format(maior))
print('Menor altura {}m'.format(menor))
