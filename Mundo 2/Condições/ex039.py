from datetime import date

atual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = atual - nascimento

if idade < 18:
    print(f'Quem nasceu em {nascimento} tem {idade} anos!')
    print(f'Ainda faltam {18 - idade} anos.')
    print(f'Seu alistamento será em {18 - idade} anos.')
elif idade == 18:
    print(f'Quem nasceu em {nascimento} tem {idade} anos!')
    print('Seu alistamento é esse ano!')
else:
    print(f'Quem nasceu em {nascimento} tem {idade} anos!')
    print(f'Você ja deveria ter se alistado há {atual - (nascimento + 18)}.')
    print(f'Seu alistamento foi em {nascimento + 18}')