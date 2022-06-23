n = int(input('Quantidade de números: '))
x = int(0)
pares = int(0)
impares = int(0)
soma_geral = int(0)
soma_pares = int(0)
for i in range (1,n+1):
    x = int(input('numero {}: '.format(i)))
    if x%2 == 0:
        pares = pares + 1
        soma_pares = soma_pares + x
    else:
        impares = impares + 1
    soma_geral = soma_geral + x
if pares == 0:
    pares = 1
media_pares = soma_pares/pares
media_geral = soma_geral/n
print('Quantidade de números pares: {}'.format(pares))
print('Quantidade de números ímpares: {}'.format(impares))
print('Média de valores pares {}: '.format(media_pares))
print('Média geral: {}'.format(media_geral))




        
