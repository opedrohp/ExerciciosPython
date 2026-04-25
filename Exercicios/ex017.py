import math
catO = float(input('Digite o comprimento do cateto oposto: '))
CatA = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = float(math.hypot(catO, CatA))
print(f'A hipotenusa do vai medir {hipotenusa:.2f}') #formatação atual