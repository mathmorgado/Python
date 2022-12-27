def decorator(funcao): # "Decora" uma função
    def wrapper():
        print('Estou antes da execução da função passada como argumento!')
        funcao()
        print('Estou depois da execução da função passada como argumento!')
    
    return wrapper


def outra_funcao():
    print('Sou a função sendo executada!')


funcao_decorada = decorator(outra_funcao)
funcao_decorada()

