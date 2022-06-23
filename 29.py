x = int(input('Você estuda? \n1-sim\n2-não\n'))
y = int(input('Você trabalha? \n1-sim\n2-não\n'))
if x == 1:
    estudo = bool(True)
if x == 2:
    estudo = bool(False)
if y == 1:
    trabalho = bool(True)
if x == 2:
    trabalho = bool(False)
if (estudo == True) and (trabalho == True):
    print('Ambas são verdadeiras')
if (estudo == False) and (trabalho == False):
    print ('Ambas são falsas')