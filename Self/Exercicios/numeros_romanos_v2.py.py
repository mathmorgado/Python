def conversor_romano(num):
    numeros_romanos = {
        1000:'M',
        900:'CM',
        500:'D',
        400:'CD',
        100:'C',
        90:'XC',
        50:'L',
        40:'XL',
        10:'X',
        9:'IX',
        5:'V',
        4:'IV',
        1:'I'
    }

    romano_convertido = ''

    for key in sorted(numeros_romanos.keys(), reverse=True):

        while num >= key:
            romano_convertido += numeros_romanos[key]
            num -= key
        
    return romano_convertido


teste = 45
print(conversor_romano(teste))