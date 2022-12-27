# Aprovar empréstimo
valor_casa = float(input('Qual o valor da casa? '))
anos = int(input('Em quantos anos pretende pagar? '))
salario = float(input('Qual seu salário? '))

parcela = anos * 12
valor_prestacao = valor_casa / parcela
percentual_salario = salario/100 * 30

if valor_prestacao > percentual_salario:
    print('O valor das prestações ultrapassaram o valor limite!')
    nova_parcela = valor_casa/percentual_salario
    valor_prestacao = valor_casa / nova_parcela
    print('Com base no seu salário, '
          f'recomendamos que parcele em {nova_parcela/12:.0f} anos, tendo como'
          f' valor máximo: R${valor_prestacao:.2f}')
else:
    print(f'O valor da prestação será de R${valor_prestacao:.2f}')
