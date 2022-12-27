def LeiaDinheiro(entrada):
    valido = False
    while not valido:
        valor = str(input(entrada).replace(',', '.')).strip()
        if valor.isalpha() or valor == '':
            print(f'\033[0;31mERROR: Valor "{valor}" não é válido!\033[m\n')
        else:
            valido = True
            return float(valor)
            
        
