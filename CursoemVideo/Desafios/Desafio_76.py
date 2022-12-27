tupla = ('Pão', 0.50, 'Ovo', 15, 'Requeijão', 13, 'Manteiga', 10, 'Café', 8,
         'Leite', 4.50, 'Mussarela', 4.50)

print(40*'-')
print(15*' ', 'LISTAGEM ', 15*' ')
print(40*'-')

cont = 0
while True:
    c = 40 - (len(tupla[cont]) + 8)
    print(tupla[cont], c*'.', 'R$', tupla[cont + 1])
    cont += 2
    if cont == 14:
        break

print(40*'-')
