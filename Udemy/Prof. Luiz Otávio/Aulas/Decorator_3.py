def parametros_decorator(nome):
    def decorator(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorator


@parametros_decorator(nome='5')
@parametros_decorator(nome='4')
@parametros_decorator(nome='3')
@parametros_decorator(nome='2')
@parametros_decorator(nome='1')
def soma(x, y):
    return x + y


dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)