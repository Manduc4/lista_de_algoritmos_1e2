ni = int(input('Número de identificação do aluno: '))
n1 = int(input('Nota 1 :'))
n2 = int(input('Nota 2:'))
n3 = int(input('Mota 3: '))
me = int(input('Média dos exercícios: '))
ma = float((n1+n2*2+n3*3+me)/7)
if ma >=90:
    conceito = str('A')
elif ma <90 and ma >=75:
    conceito = str('B')
elif ma <75 and ma >=60:
    conceito = str('C')
elif ma <60 and ma>=45:
    conceito = str('D')
elif ma < 40:
    conceito = str('E')
if conceito == 'A' or 'B' or 'C':
    resultado = str('Aprovado')
elif conceito == 'D' or 'E':
    resultado = str('Reprovado')
print('Número do aluno: {}'.format(ni))
print('Nota 1:{}'.format(n1))
print('Nota 2: {}'.format(n2))
print('Nota 3: {}'.format(n3))
print('Média dos exercícios: {}'.format(me))
print('Média de aproveitamento: {}'.format(ma))
print('Conceito: {}, {}'.format(conceito,resultado))