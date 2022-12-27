n = int(input('Digite um número inteiro qualquer: '))
lista = [0, 1]
f = 1

while len(lista) != n:
    f += lista[-2]
    lista.append(f)

print(lista)
