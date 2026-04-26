from time import sleep
velocidade = float(input('Qual é a velocidade do carro? '))
multa = (velocidade - 100) * 7
print('AGUARDE...')
sleep(2)
if velocidade > 100:
    print('MULTADO! Você excedeu o limite permitido que é de 100Km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}')
    print('Tenha um bom dia!')
else:
    print('Tenha um bom dia!')