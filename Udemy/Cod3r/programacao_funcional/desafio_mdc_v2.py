# Solução do professor
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
