from time import sleep


def contador(inicio, fim, passo):
    if '-' not in str(passo) and inicio > fim:
        passo = f'-{passo}'
    if passo == 0:
        passo = 1

    print('-='*25)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')

    for i in range(inicio, fim, int(passo)):
        print(i, end=' ', flush=True)
        sleep(0.25)
    print('')


contador(1, 10, 1)
contador(10, 1, 2)
print('-='*25)

inicio = int(input('Agora é sua vez!\n  Início: '))
fim = int(input('  Fim: '))
passo = int(input('  De: '))

contador(inicio, fim, passo)
