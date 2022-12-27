while True:
    n = int(input('Digite um número inteiro e informarei sua tabuada: '))
    c = 1
    if n < 0:
        break
    while c != 11:
        print(f'{n} x {c} = {n * c}')
        c += 1

print('Cabo!')
