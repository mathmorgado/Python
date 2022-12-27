import random

lista = random.sample(range(1, 100), 50)

num_escolhido = int(input('Escolha um número: '))

if num_escolhido not in lista:
    lista.append(num_escolhido)

lista.sort()

while True:
    resposta = str(input(f'Seu número é maior que {len(lista) / 2}[S/N]? '))
    if resposta in 'Ssim':
        del lista[0:len(lista)/2]
    else:
        del lista[len(lista)/2:]
    print(lista)
