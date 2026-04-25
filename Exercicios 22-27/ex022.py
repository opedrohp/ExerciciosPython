nome = str(input('Digite seu nome completo: ')).strip() #strip sem argumentos remove os espaços em branco antes e depois
print('Analisando seu nome...')
print(f'seu nome em maiusculas: {nome.upper()}')
print(f'seu nome em minusculas: {nome.lower()}')
print(f'Seu nome tem {len(nome)} letras') # len retorna o tamanho do objeto, no caso 'nome'

separa = nome.split() # Se nenhum argumento for fornecido, split()a string será separada por qualquer espaço em branco (espaços, tabulações, novas linhas) e strings vazias serão descartadas automaticamente do resultado.
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')