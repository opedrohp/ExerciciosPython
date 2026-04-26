from math import radians, sin, cos, tan
angulo = float(input('Digite um angulo: '))

cosseno = cos(radians(angulo))
tangente = tan(radians(angulo)) # criar variaval para declaração de valor

print(f'O angulo de {angulo:.0f} tem o SENO de {sin(radians(angulo)):.2f}') #declaraçao de valor junto com print
print(f'O angulo de {angulo:.0f} tem o COSSENO de {cosseno:.2f}')
print(f'O angulo de {angulo:.0f} tem a TANGENTE de {tangente:.2f}')