ex = str(input('Digite uma expressão numérica usando parênteses: '))

if '(' in ex and ')' in ex:
    if (ex.count('(') + ex.count(')')) % 2 == 0:
        print('A expressão é válida!')
    else:
        print('A expressão não é válida')
