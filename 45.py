n = int(input('Tabuada que deseja calcular: '))
for i in range(1,11):
    resultado = n * i
    print ('{} . {} = {}'.format(i,n,resultado))