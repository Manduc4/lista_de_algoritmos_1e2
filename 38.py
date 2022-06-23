n = int(1)
soma = int(0)
while n < 500:
    if n%3 == 0:
        soma = soma + n
        print('numero', n,' soma ',soma)
    n += 2
print('Soma final = {}'.format(soma))