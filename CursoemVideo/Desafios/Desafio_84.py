pessoas = []
pesado = []
leve = []

cont = 0

while True:
    print(30 * '-')
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    pessoas.append(nome)
    pessoas.append(peso)
    if cont == 0:
        pesado.append(pessoas[:])
        leve.append(pessoas[:])
    else:
        if pessoas[-1] < leve[0][1]:
            leve.pop()
            leve.append(pessoas[-2:])
        if pessoas[-1] > pesado[0][1]:
            pesado.pop()
            pesado.append(pessoas[-2:])
    cont += 1
    resp = str(input('Deseja continuar[S/N]? '))
    if resp in 'Nn':
        break

print(f'\nDentre as {len(pessoas)/2:.0f} cadastradas, a mais pesada é', end='')
print(f' {pesado[0][0]}, com {pesado[0][1]} Kg.')
print(f'Já a mais leve é {leve[0][0]}, com {leve[0][1]} Kg')
