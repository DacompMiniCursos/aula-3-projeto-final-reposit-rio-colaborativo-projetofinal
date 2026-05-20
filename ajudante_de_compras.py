print("Digite o saldo disponível e o valor dos produtos que você quer comprar. Quando terminar de listar os valores, digite 0 para ver se pode ou não comprar os produtos.
print("")

saldo_usuario = float(input('Qual o seu saldo? '))

while True:
    valor_produto = float(input('Valor do produto: '))
    if valor_produto == 0:
        break

if valor_produto>= 100:
    valor_produto= valor_produto+valor_produto/10
saldo_restante = saldo_usuario - valor_produto

if saldo_restante >= 0:
    print('Pode comprar!')
    
else:
    print('Não pode comprar.')

# autores
Lucas e Victor
