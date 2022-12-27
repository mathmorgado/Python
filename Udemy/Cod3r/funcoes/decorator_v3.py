def log(function):
    def decorator(*args, **kargs):  # Aceita qualquer argumento!
        print(f'Inicio da chamada da função: {function.__name__}')
        print(f'args: {args}')
        print(f'kargs: {kargs}')
        resultado = function(*args, **kargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator


@log
def soma(x, y):
    return x + y

@log
def sub(x, y):
    return x - y


if __name__ == '__main__':
    print(soma(5, 3))
    print(sub(7, y=7))