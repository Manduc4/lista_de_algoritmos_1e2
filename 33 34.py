h = float(input('Altura: '))
peso = float(input('Peso: '))
imc = float(peso/(h**2))
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Seu peso está na faixa da normalidade')
elif imc >=25 and imc < 30:
    print('Você está acima do peso')
elif imc >= 30:
    print('Você está obeso')
