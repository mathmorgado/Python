def mapear(funcao, lista):
    return ( funcao(valor) for valor in lista)

if __name__ == '__main__':
    print(tuple(mapear( lambda x: x**2, [2, 3, 4] )))