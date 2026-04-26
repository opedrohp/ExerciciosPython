print('{:=^40}'.format(' LOJAS '))
compras = int(input('Preço das compras: R$'))
print('-'*40)
print('FORMA DE PAGAMENTO')
print('-'*40)
print('[1] à vista dinheiro/cheque')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
print('-'*40)
opcao = int(input('Qual é a opção de pagamento?'))


if opcao == 1:
    total = compras - (compras * 10 / 100)
    print(f'Sua compra de R${compras:.2f} vai custar R${total:.2f} no final.')
elif opcao == 2:
    total = compras - (compras * 5 / 100)
    print(f'O valor total da compra foi R${total:.2f} no final.')
elif opcao == 3:
    total = compras
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} sem juros.')
elif opcao == 4:
    total = compras + (compras * 20 / 100)
    totparcelas = int(input('Quantas parcelas? '))
    parcelas = total / totparcelas
    print(f'Sua compra será parcelada em {totparcelas}x de R${parcelas} com juros.')
    print(f'Sua compra de R${compras:.2f} vai custar R${total:.2f} no final.')
else:
    total= 0
    print('Opção invalida de pagamento. Tente novamente')