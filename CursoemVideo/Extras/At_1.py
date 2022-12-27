from random import randint

lista = []
menores = []

while len(menores) < 2:
    while True:
        lista.append(randint(0, 50))
        if len(lista) == 1:
            menor = lista[0]
        else:
            if lista[-1] == lista[-2]:
                del(lista[-1])
        if lista[-1] < menor:
            menor = lista[-1]
        if len(lista) >= 10:
            break
    print(lista, f'\nO menor valor da lista é: {menor}\n')
    menores.append(menor)
    lista.clear()

print(f'\nOs menores valores de ambas as listas são: {menores}')
