saldo_usuario = float(input('Produto: '))
valor_produto = float(input('Valor: '))

saldo_restante = saldo_usuario - valor_produto

if saldo_restante >= 0:
    print('Pode comprar!')
    
else:
    print('Não pode comprar.')
