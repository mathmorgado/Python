def obter_valor_monetario():
    while True:
        valor = input('Digite um valor: R$').replace(',', '.')

        try:
            valor = float(valor)
            return valor
        except ValueError:
            print('Por favor, digite um número válido! Ex: 3215,80\n')


def calcular_cedulas(valor):
    notas = [100, 50, 20, 10, 5, 2]
    qtde = 0

    print('\nNOTAS')
    while valor >= 2:
        for nota in notas:
            if valor >= nota:
                valor -= nota
                qtde += 1
                break
        else:
            print(f'{qtde} notas de R${nota:.2f}')
            qtde = 0
            notas.pop(0)
    print(f'{qtde} notas de R${nota:.2f}')


def calcular_moedas(valor):
    moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
    qtde = 0

    print('\nMOEDAS')
    while valor > 0:
        for moeda in moedas:
            if round(valor, 2) >= moeda:
                valor = round(valor, 2) - moeda
                qtde += 1
                break
        else:
            print(f'{qtde} moedas de R${moeda:.2f}')
            qtde = 0
            moedas.pop(0)
    print(f'{qtde} moedas de R${moeda:.2f}')


valor = obter_valor_monetario()
calcular_cedulas(valor)
calcular_moedas(valor)
