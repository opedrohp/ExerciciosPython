peso = float(input('Qual é o seu peso?'))
altura = float(input('Qual é a sua altura?'))
imc = peso / (altura * altura)
print(f'O IMC dessa pessoa é {imc:.1f}')

if imc < 18.5:
    print('Cuidado! Você está abaixo do peso!')
elif imc >= 18.5 and imc <= 25:
    print('Parabéns! Você está na faixa de peso normal')
elif imc >= 25 and imc <= 30:
    print('Cuidado! Você está acima do peso')
else:
    print('Você está em OBESIDADE MORBIDA, cuidado!')