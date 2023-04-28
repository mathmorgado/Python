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
