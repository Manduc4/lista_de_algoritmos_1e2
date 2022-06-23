h = float(input('Altura (em metros): '))
sexo =int(input('Sexo:\n1-Masculino\n2-Feminino\n'))
if sexo == 1:
    peso_ideal = float(72.7*h)-58
    print('Seu peso ideal é {} Kg'.format(peso_ideal))
elif sexo == 2:
    peso_ideal = float(62.1*h)-44.7
    print('Seu peso ideal é {} Kg'.format(peso_ideal))