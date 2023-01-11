def multiplicacao(*args):
    total = 1
    for num in args:
        total *= num
    return total    


def par_impar(num):
    return 'PAR' if num % 2 == 0 else 'ÍMPAR'


multiplicados =  multiplicacao(2, 3, 4, 5)

print(multiplicados)
print(par_impar(7))