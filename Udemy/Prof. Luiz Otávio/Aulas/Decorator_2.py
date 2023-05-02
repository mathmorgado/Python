def fabrica_de_decoradores(a=None, b=None, c=None):
    def decoradora_de_funcoes(func):

        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador: ', a, b, c)
            res = func(*args, **kwargs)
            return res
        
        return aninhada
    
    return decoradora_de_funcoes  # Acesso a 3 escopos diferentes


@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    print('Nome da função: ', soma.__name__) # Retorna nome = 'aninhada' pq o python faz a função 'soma' virar a 'aninhada'
    return x + y


decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)