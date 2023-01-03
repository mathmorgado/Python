def cores_arco_iris():
    yield 'Vermelho'
    yield 'Alaranjado'
    yield 'Amarelo'
    yield 'Verde'
    yield 'Azul'
    yield 'Anil'
    yield 'Violeta'

if __name__ == '__main__':
    generator = cores_arco_iris()
    print(type(generator))
    while True:
        print(next(generator))
    