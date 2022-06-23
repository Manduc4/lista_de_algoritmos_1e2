x = int(input('Digite um número de até 3 algarismos: '))
centena = int(x//100)
dezena = int(x%100)//10
unidade = int((x%100)%10)
print ('CENTENA: ', centena)
print('\nDEZENA: ', dezena)
print('\nUNIDADE: ', unidade)
