num = int(input('Escolha um número e irei lhe mostrar sua tabuada: '))

for c in range(1, 11):
    tabuada = num * c
    print(f'{num} x {c} = {tabuada}')
