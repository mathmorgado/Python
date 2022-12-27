lista = []
par = []
impar = []

while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar: '))
    if resp in 'NnAaOo':
        break

for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])

lista.sort()

print(f'\nA lista dos números digitados é: {lista}')
print(f'Dos números digitados, são pares os: {par}')
print(f'Dos números digitados são impares os: {impar}')
