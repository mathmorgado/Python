"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

def verificador_cpf(cpf):
    digitos_cpf = ''.join(cpf.split('-')[0].split('.'))
    produto_multiplicacao = 0
    multiplicador = 10

    for digito in digitos_cpf:
        produto_multiplicacao += int(digito) * multiplicador
        multiplicador -= 1
    
    primeiro_digito = (produto_multiplicacao * 10) % 11

    if primeiro_digito > 9:
        primeiro_digito = 0
        
    if str(primeiro_digito) == cpf.split('-')[1][0]:
        digitos_cpf += str(primeiro_digito)
        produto_multiplicacao = 0
        multiplicador = 11
        
        for digito in digitos_cpf:
            produto_multiplicacao += int(digito) * multiplicador
            multiplicador -= 1
        
        segundo_digito = (produto_multiplicacao * 10) % 11

        if str(segundo_digito) == cpf.split('-')[1][1]:
            print('CPF VÁLIDO')
        else:
            print('\033[31mCPF INVÁLIDO!\033[m')

    else:
        print('\033[31mCPF INVÁLIDO!\033[m')


verificador_cpf('131.805.026-06')
    