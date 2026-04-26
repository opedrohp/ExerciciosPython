salario = float(input('Qual o seu salario: '))
if salario <= 1250:
    aumento = salario * 1.15
    print(f"Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f}")
else:
    aumento = salario * 1.10
    print(f"Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f}")


