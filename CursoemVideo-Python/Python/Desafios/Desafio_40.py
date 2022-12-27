nota_semestre1 = float(input('Informe sua nota do primeiro semestre: '))
nota_semestre2 = float(input('Informe sua nota do segundo semestre: '))
media = (nota_semestre1 + nota_semestre2) / 2

if media < 5:
    print('Você foi reprovado!')
elif media >= 5 and media <= 6.9:
    print('Você está de recuperação!')
elif media == 10:
    print('Você tirou nota maxima, parabéns!')
else:
    print('Você passou!')
