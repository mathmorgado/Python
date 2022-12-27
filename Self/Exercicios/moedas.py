"""
Passo 1: Tratar valor
Passo 2: Pegar valor tratado
Passo 3: Defenir notas/moedas
Passo 4: Definir condição que subtrair do valor apenas notas/moedas menores
Passo 5: Exibir quantas notas/moedas de cada foram usadas
"""


def is_moeda(valor):
    while True:
        valor = input('Digite um valor: R$').replace(',', '.')

        try:
            valor = float(valor)
            return valor
        except ValueError:
            print('Por favor, Digite um núemro válido! Ex: 35,80\n')
            continue


notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

valor = is_moeda('Digite um valor: R$')
qtde = 0

while True:
    if valor < 2 and valor >= 1:
        print(f'{qtde} notas de R${nota}')
        qtde = 0
        break

    for nota in notas:
        if valor // nota:
            valor -= nota
            qtde += 1
            break
        else:
            notas.remove(notas[0])
            print(f'{qtde} notas de R${nota}')
            qtde = 0
            break

while True:
    if valor == 0:
        print(f'{qtde} moedas de R${moeda}')
        break

    for moeda in moedas:
        if round(valor, 2) // moeda:
            valor = round(valor, 2) - moeda
            qtde += 1
            break
        else:
            moedas.remove(moedas[0])
            print(f'{qtde} moedas de R${moeda}')
            qtde = 0
            break
