from random import sample

tupla = tuple(sample(range(10), 5))
mm = sorted(tupla)
print(tupla)
print(f'O menor valor aleatório da tupla é {mm[0]} e o maior {mm[-1]}.')
