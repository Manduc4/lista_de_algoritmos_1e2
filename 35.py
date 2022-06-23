preco_normal = float(input('Preço da etiqueta: R$'))
opcao = int(input('Escolha uma opção de pagamento:\n1- À vista em dinheiro ou cheque\n2- À vista no cartão de crédito\n3- Em duas vezes\n4- Em duas vezes\n'))
if opcao == 1:
    preco_final = preco_normal - 0.10*preco_normal
    print(preco_final,' reais')
elif opcao == 2:
    preco_final = preco_normal - 0.15*preco_normal
    print(preco_final,' reais')
elif opcao == 3:
    preco_final = preco_normal
    print(preco_final,' reais')
elif opcao == 4:
    preco_final = preco_normal + 0.10 * preco_normal
    print(preco_final, 'reais')