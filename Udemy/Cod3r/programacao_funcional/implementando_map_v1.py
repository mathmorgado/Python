def mapear(funcao, lista):
    for valor in lista:
        yield funcao(valor)
    

if __name__ == '__main__':
    print(tuple(mapear( lambda x: x**2, [2, 3, 4] )))