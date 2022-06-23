a = int(input('Número que deseja calcular o fatorial: '))
fatorial = int(1)
i = int(1)
for i in range(1,a+1):
    fatorial = fatorial * i
    print(fatorial)