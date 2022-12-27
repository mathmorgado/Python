lista = []

for c in range(1, 6):
    num = int(input('Digite um valor: '))
    if c == 1 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1

print(f'Os valores digitados em ordem fica: {lista}')
