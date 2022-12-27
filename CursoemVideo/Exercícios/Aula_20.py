def soma(a=4, b=3):
    print(f'{a} - {b} = {a-b}')


soma()
soma(9, 5)
soma(b=9, a=5)


def contador(*nums):
    soma = 0
    for n in nums:
        soma += n
    print(f'\nAo todo são {len(nums)} parâmetros e a soma é: {soma}')


contador(5, 3, 2, 6, 7, 9)


def dobro(lst):
    posicao = 0
    while posicao < len(lst):
        lst[posicao] *= 2
        posicao += 1
    print(lst)
    # Or just -> "return [m * 2 for m in lst]"


lista = [2, 4, 6, 8, 10]
print(dobro(lista))
