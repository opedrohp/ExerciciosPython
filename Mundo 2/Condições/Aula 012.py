nome = str(input('Qual é o seu nome? '))
if nome == 'Paulo':
    print('Que nome bonito!')
elif nome == 'Pedro':
    print('Seu nome é o melhor que existe')
elif nome in 'Isadora Sophia Julia':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia {nome}')