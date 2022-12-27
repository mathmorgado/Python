homem = 0
mulher20 = 0
maior = 0

while True:
    print('\n__ Cadastre uma pessoa __')
    idade = int(input('Idade: '))
    sexo = str(input('Gênero[M/F]: '))

    while sexo not in 'MmFf':
        sexo = str(input('Gênero[M/F]: '))

    print(25 * '-')

    if sexo in 'Mm':
        homem += 1
    elif sexo in 'Ff' and idade <= 20:
        mulher20 += 1
    if idade >= 18:
        maior += 1

    resp = str(input('Deseja continuar[S/N]? '))
    if resp in 'Nn':
        break

    while resp not in 'SsNn':
        resp = str(input('Deseja continuar[S/N]? '))

print(f'Maior de idade: {maior}\nHomens: {homem}\nMulher menos 20: {mulher20}')
