# Genarator é uma função que pausa, frequentemente usado para produzir uma grande sequência de valores, mas sem armazenar tudo na memória de uma vez
import sys

generator = (n for n in range(1000000))
lista = [n for n in range(1000000)]

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))