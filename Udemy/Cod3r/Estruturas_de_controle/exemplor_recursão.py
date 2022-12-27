def imprimir(maximo, atual):
    if atual <= maximo:
        print(atual)
        imprimir(maximo, atual + 1)
        return


imprimir(100, 50)
