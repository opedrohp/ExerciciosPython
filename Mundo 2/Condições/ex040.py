n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
mediaNota = (n1 + n2) / 2
mediaAprov = 7
if mediaNota >= mediaAprov:
    print(f'Tirando {n1} e {n2}, a média do aluno é {mediaNota}')
    print('Aprovado')
elif mediaNota < mediaAprov and mediaNota >= 6:
    print(f'Tirando {n1} e {n2}, a média do aluno é {mediaNota}')
    print('Ficou em recuperação')
else:
    print(f'Tirando {n1} e {n2}, a média do aluno é {mediaNota}')
    print('Reprovado')
