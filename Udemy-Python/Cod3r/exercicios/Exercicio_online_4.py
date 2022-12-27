ano = int(input('Quantos anos você tem? '))
mes = int(input('Qual mês você nasceu? (numerico) '))
dia = int(input('Que dia? '))

conversao_ano = ano * 365
conversao_mes = mes * 30

idade_dias = conversao_ano + conversao_mes + dia
print(f'Você viveu aproximadamente {idade_dias} dias, uau!')
