nota = 7

if nota >= 9:
    print('Quadro de honra')
elif nota >= 7:
    print('Aprovado!')
elif nota >= 5:
    print('Recuperação!')
else:
    print('Reprovado!')

if nota.isnumeric():
    print(30 * 's')
