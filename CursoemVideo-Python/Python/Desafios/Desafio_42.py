print('A seguir, iremos pedir três segmentos de reta e iremos'
      'lhe informar se as medidas fornecidas formam um triângulo.')

segmento1 = float(input('Informe o valor do primeiro segmento: '))
segmento2 = float(input('Informe o valor do segundo segmento: '))
segmento3 = float(input('Informe o valor do terceiro segmento: '))

if (segmento1 + segmento2) >= segmento3:
    if (segmento1 + segmento3) >= segmento2:
        if (segmento2 + segmento3) >= segmento1:
            print('As medidas fornecidas possibilitam um triangulo')
            if segmento1 == segmento2 == segmento3:
                print('O triangulo formado será Equilátero')
            elif segmento1 == segmento2 and segmento3 != segmento1:
                print('O triangulo formado será Isósceles')
            elif segmento1 == segmento3 and segmento2 != segmento3:
                print('O triangulo formado será Isósceles')
            elif segmento3 == segmento2 and segmento1 != segmento3:
                print('O triangulo formado será Isósceles')
            else:
                print('O triangulo formado será Escaleno')
        else:
            print('As medidas fornecidas não formam um triangulo')
    else:
        print('As medidas fornecidas não formam um triangulo')
else:
    print('As medidas fornecidas não formam um triangulo')
