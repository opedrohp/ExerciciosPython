L = float(input('Qual a largura da parede em metros: '))
A = float(input('Qual a altura da parede em metros: '))
area = L*A
Tinta = area/2
print('Sua parede tem a dimensão de {:.2f} x {:.2f} e sua área é de {:.2f}m2 . Para pintar essa parede, você precisará de {:.2f}L de tinta.'.format(L,A,area,Tinta))