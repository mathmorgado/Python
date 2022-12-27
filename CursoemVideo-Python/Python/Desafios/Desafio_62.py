print('A seguir iremos realizar um PA (progressão aritmética). ')
pri_termo = int(input('Defina o 1º termo: '))
razao = int(input('Defina a razão: '))
pa = pri_termo
c = 1

while c != 11:
    print(f'|{c}º termo - {pa}')
    pa = pa + razao
    c += 1

con = int(input('\nQuantos Termos você deseja ver agora? '))
n = 1

if con == 0:
    exit()

else:
    for m in range(1, con + 1):
        term = int(input(f'\nEscolha o {m}º termo: '))
        pa = term
        c = 1
        while c != 11:
            print(f'|{n}º termo - {pa}')
            n += 1
            pa += razao
            c += 1
