dicionario = {i: i * 2 for i in range(1, 11) if i % 2 == 0}
print(dicionario)

for numero, dobro in dicionario.items():
    print(f'{numero} x 2 = {dobro}')
