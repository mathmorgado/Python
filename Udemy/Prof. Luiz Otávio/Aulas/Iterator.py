import sys

# Iterables e Iterators em Python
iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable) #  tem __iter__ e __next__ /iterator só sabe qual é o próximo valor do iteravél

# 'for' na mão
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

