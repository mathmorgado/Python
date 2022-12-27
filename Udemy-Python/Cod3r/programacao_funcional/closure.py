def multiplicar(x):
    def calcular(y): # tem consciencia do local que foi definida (dentro de outra funcao)
        return x * y # devido a consciencia do local, tem acesso a parâmetros 'vizinhos'
    return calcular # Retorna uma função (funcao de alta ordem)


if __name__ == '__main__':
    dobro = multiplicar(2)
    triplo = multiplicar(3) # definindo o x

    print(dobro, triplo)

    print(f'O triplo de 5 é {triplo(5)}') # definindo y
    print(f'O dobro de 7 é {dobro(7)}')