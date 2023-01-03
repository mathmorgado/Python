from functools import reduce
from operator import add

valores =[20, 33, 11, 81, 9, 112]

print(f'Lista: {valores}')

# Funções de imutabilidade
print(f'\nOrdem crescente: {sorted(valores)}')
print(f'Menor valor: {min(valores)}')
print(f'Maior valor: {max(valores)}')
print(f'Lista revertida: {tuple(reversed(valores))}')
print(f'Soma da lista(sum): {sum(valores)}')
print(f'Soma da lista(reduce): {reduce(add, valores)}')