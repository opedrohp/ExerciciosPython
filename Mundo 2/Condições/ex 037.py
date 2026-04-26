while True:
    try:

        n1 = int(input('Digite um numero inteiro: '))
        print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
[ 0 ] sair do programa''')
        opcao = int (input('Sua opção: '))
        if opcao == 1:
            print(f'{n1} convertido para BINÁRIO é igual a {bin(n1)[2:]} ')
        elif opcao == 2:
            print(f'{n1} convertido para OCTAL é igual a {oct(n1)[2:]} ')
        elif opcao == 3:
            print(f'{n1} convertido para HEXADECIMAL é igual a {hex(n1)[2:]} ')
        elif opcao == 0:
            print('Saindo do programa...')
            break
        else:
            print('Opção invalida!')
    except ValueError:
        print('Digite um numero inteiro valido!')
#Fiz um loop extra pra nao precisar ficar rodando o programa toda hora pra testar as opções, mas o exercicio pede pra trabalhar somente com condiçoes aninhadas