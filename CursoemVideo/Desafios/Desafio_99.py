from time import sleep
print('-='*30)


def maior(*list):
    print('Analisando os valores passados...')
    for valor in list:
        print(valor, end=' ', flush=True)
        sleep(0.25)
    print(
        f'Foram informados {len(list)} números e o maior é {sorted(list)[-1]}')
    print('-='*30)


maior(1, 2, 3, 4, 5, 6, 7, 8, 9)
maior(45, 8, 31, 62, 44, 5)
