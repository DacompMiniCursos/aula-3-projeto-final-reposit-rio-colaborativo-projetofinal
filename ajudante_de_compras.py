saldo_usuario = float(input('Produto: '))
valor_produto = float(input('Valor: '))

if valor_produto>= 100:
    valor_produto= valor_produto+valor_produto/10
saldo_restante = saldo_usuario - valor_produto

if saldo_restante >= 0:
    print('Pode comprar!')
    
else:
    print('Não pode comprar.')
# autores
Lucas e Victor
