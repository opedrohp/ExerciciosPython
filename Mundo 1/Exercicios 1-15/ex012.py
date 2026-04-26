p1 =float(input("Qual é o preço do produto? R$"))
resultado = p1 - (p1 *5/100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(p1,resultado))