list = []

for c in range(3, 501, 6):
    list.append(c)

print(f'A soma de todos os multiplos de três entre 1 e 500 é: {sum(list):,}')
