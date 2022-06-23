salario_inicial = float(input('Salário inicial: R$'))
salario_aumentado = salario_inicial * 1.15
salario_final = salario_aumentado - 0.08 * salario_aumentado
print ('Salario inicial: R$', salario_inicial)
print('Salario com aumento: R$', salario_aumentado)
print('Salario final: R$', salario_final)