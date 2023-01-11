"""
Listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
"""
#     0  1  2  3  4  5  6  7  8
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('Fatiamentos =', l2[2:6], ' e ', l2[::-1] )

# Append x Extend x Insert

x = (11, 12)
y = (13, 14)

l2.extend(x)  # Adiciona todos os elementos interavéis no final

print('Extend =', l2 )

l2.append(y)  # Adiciona um elemento interavel no final

print('Append =', l2 )

l2.insert(9, 10) # Insere um valor no index definido

print('Insert =', l2 )

# Pop x Del x Clear

l2.pop()  # Exclui o último

print('Pop =', l2 )

del(l2[9:])  # Excluí os elementos selecionados

print('Del =', l2 )

l2.clear()  # Limpa toda a lista

print('Clear =', l2 )

# Max x Min

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('max =', max(lista))
print('min =', min(lista))

# prática

lis = list(range(0, 51, 5))

print(lis)

lis.insert(0, max(lis))
del(lis[-1])

print('maior valor no início =', lis)
