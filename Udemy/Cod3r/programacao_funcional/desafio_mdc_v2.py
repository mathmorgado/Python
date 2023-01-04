"""
Passo 1: Pegar o menor valor
passo 2: Testar se são todos os itens da lista são divisiveis por ele
passo 3: Diminuir de 1 em 1 até achar o valor que divide todos
"""
def mdc(lista): # Minimo divisor comum
    def calc(divisor):
        return divisor if sum(map(lambda x: x % divisor, lista)) == 0 else calc(divisor - 1)
    return calc(min(lista))

if __name__ == '__main__':
    print(mdc([21, 7])) # 7
    print(mdc([125, 40])) # 5
    print(mdc([9, 564, 66, 3])) # 3
    print(mdc([55, 22])) # 11
    print(mdc([15, 150])) # 15
    print(mdc([9, 7])) # 1
