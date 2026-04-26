print('-=-'*20)
print('Analisador de Triangulos')
print('-=-'*20)
r1 = float(input('Primeiro valor: '))
r2 = float(input('Segundo valor: '))
r3 = float(input('Terceiro valor: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar triangulos')
else:
    print('Os segmentos acima não podem formar triangulos')