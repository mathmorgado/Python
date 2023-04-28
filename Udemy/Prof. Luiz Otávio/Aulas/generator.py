# Genarator é uma função que pausa, frequentemente usado para produzir uma grande sequência de valores, mas sem armazenar tudo na memória de uma vez
import sys

generatorr = (n for n in range(1000000))
lista = [n for n in range(1000000)]

# print(sys.getsizeof(lista)) -> 8448728kb
# print(sys.getsizeof(generatorr)) -> 11kb

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n > maximum:
            return n

        
gen = generator(n=0)

for n in gen:
    print(n)

# Yield from
def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')


def gen3():
    print('COMECOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')


def gen2(gen=None):
    print('COMECOU GEN2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()

for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()