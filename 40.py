i, quant_numeros, n = int(0)
porcentagem_p, porcentagem_n, n_positivos, n_negativos, media, soma = float(0)
quant_numeros = int(input('Quantidade de números: '))
for i in range(1,quant_numeros + 1):
    n = int(input('Número {}'.format(i)))
    soma = soma + n
    if n > 0:
        n_positivos = n_positivos + 1
    elif n < 0:
        n_negativos = n_negativos + 1





