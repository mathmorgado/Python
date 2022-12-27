w = int(input('Digite um valor: '))
x = int(input('Digite um valor: '))
y = int(input('Digite um valor: '))
z = int(input('Digite um valor: '))

tupla = (w, x, y, z)
contagem = tupla.count(9)
contagem3 = tupla.count(3)


print(tupla)

if contagem > 0:
    print(f'O numero 9 aparaceu {contagem} vezes')
else:
    print('Nenhum valor 9 digitado!')

if contagem3 > 0:
    posicao = tupla.index(3)
    print(f'O numero 3 aparece na {posicao + 1}º posição')
else:
    print('Nenhum valor 3 digitado!')
