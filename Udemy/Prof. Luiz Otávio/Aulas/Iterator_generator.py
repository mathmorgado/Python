import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable) #  tem __iter__ e __next__ /iterator só sabe qual é o próximo valor do iteravél

# 'for' na mão
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

generator = (n for n in range(1000000))
lista = [n for n in range(1000000)]

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))