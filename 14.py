preco_produto = float(input('Preço do produto: '))
valor_pago = float(input('Valor pago:'))
resultado = float(preco_produto - valor_pago)
if resultado == 0:
    print('Tudo certo, tenha um bom dia !!!')
if resultado < 0:
    print('Seu troco é', -resultado, 'Reais')
if resultado > 0:
    print('Faltam', resultado, 'Reais')
    valor_pago += float(input('Entregue o valor restante:'))
    if valor_pago == preco_produto:
        print('Tudo certo, tenha um bom dia!!!')
