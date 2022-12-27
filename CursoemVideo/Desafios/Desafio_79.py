lista = list()

for c in range(1, 11):
    lista.append(int(input('Digite um valor: ')))
    if lista[-1] in lista[:-1]:
        del lista[-1]

lista.sort()
print(lista)
