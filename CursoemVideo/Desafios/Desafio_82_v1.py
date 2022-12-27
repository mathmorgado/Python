lista = []
par = []
impar = []

while True:
    n = int(input('Digite um valor: '))
    resp = str(input('Deseja continuar: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    if resp in 'NnAaOo':
        break

lista.sort()

print(f'\nA lista dos números digitados é: {lista}')
print(f'Dos números digitados, são pares os: {par}')
print(f'Dos números digitados são impares os: {impar}')
