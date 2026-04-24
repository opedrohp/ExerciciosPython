carteira = float(input('Quanto dinheiro você tem na carteira: R$ '))
dolar = carteira / 5.03
print('Com R${} você pode comprar US${:.2f}'.format(carteira,dolar))