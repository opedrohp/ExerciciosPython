n1 = float (input('Informe um número: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print(f'Analisando o numero {n1:.0f} ...')
print(f'unidade: {u:.0f}')
print(f'dezena: {d:.0f}')
print(f'centena: {c:.0f}')
print(f'milhar: {m:.0f}')
