# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático) pq facilita a vida

def criar_funcao(func): # funcao decoradora
    def interna(*args, **kwargs): # funcao a ser retornada sem ser executada
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna


@criar_funcao # syntax sugar
def inverte_string(string): # funcao a ser deocrada
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


# inverte_string_checando_parametro = criar_funcao(inverte_string) ->  Sem o decorator @
# invertida = inverte_string_checando_parametro('123') -> Sem o decorator @
invertida = inverte_string('123')
print(invertida)