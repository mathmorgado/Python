"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +, min, max
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Luiz Otávio',  1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))

"""
Fatiamento de Listas em python

    -Métodos-
append - Adiciona um item ao final
insert - Adiciona um item ao índice escolhido
pop - Remove do final ou do índice escolhido e pode retornar o valor
del - Apaga um índice
clear - Limpa a lista
extend - Estende a lista
+ - Concatena as listas
min - Pega o maior valor da lista
max - Pega o menor valor da lista
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

ultimo_valor_removido = l2.pop()  # Exclui por padrão o último elemento e pode retornar ele numa variavel

print( 'Pop =', l2, 'Pop removido =', ultimo_valor_removido )

del(l2[9:])  # Excluí os elementos selecionados

print( 'Del =', l2 )

l2.clear()  # Limpa toda a lista

print( 'Clear =', l2 )

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

"""
Cuidados com dados mutáveis
= - Em dados imutáveis, o valor é 'copiado' 
= - Em dados mutaveis, se aponta para o mesmo valor na memória
"""
lista_a = ['Luiz', 'Maria']
lista_b = lista_a  # Usando a função 'copy', o problema é resolvido!

lista_a[0] = 'Qualquer coisa'
print(f'\n{lista_a}')
print(f'{lista_b}')

"""
Empacotamento e desempacotamento
"""
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)