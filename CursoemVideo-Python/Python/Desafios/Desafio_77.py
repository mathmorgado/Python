tupla = ('LEAO', 'CABRA', 'BOI', 'COBRA', 'DINHEIRO', 'GOSTOSO', 'REI', 'MEDO')

print(tupla)

for p in tupla:
    print(f'\nNa palavra {p} temos ', end=(''))
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
