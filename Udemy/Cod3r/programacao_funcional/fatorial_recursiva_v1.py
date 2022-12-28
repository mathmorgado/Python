# Solução que fiz

def fatorial_normal(num):
    fat = num - 1
    resultado = num * fat

    while fat > 1:
        fat1 = fat - 1
        fat -= 2
        resultado *=  (fat1 * fat)

    return resultado


def fatorial_recursiva(num, res=1):
    fat = num - 1
    res *= num * fat

    while fat > 1:
        resultado = res
        return fatorial_recursiva(num=(fat - 1), res=resultado)
        
    return res


if __name__ == '__main__':
    print(fatorial_normal(10))
    print(fatorial_recursiva(10))