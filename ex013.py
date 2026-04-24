salario = float(input('Qual o seu salario? R$ '))
aumento = salario + (salario * 15 / 100)
print('O salario que era R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario,aumento))