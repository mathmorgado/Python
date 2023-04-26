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
    pri_digit_verificado = False

    while True:
        if pri_digit_verificado:
            digitos_cpf += str(valor_digito)
            digito_verificar = 1
            produto_multiplicacao = 0
            multiplicador = 11
            cpf_valido = True
        else:
            digitos_cpf = ''.join(cpf.split('-')[0].split('.'))
            digito_verificar = 0
            produto_multiplicacao = 0
            multiplicador = 10
            cpf_valido = False

        for digito in digitos_cpf:
            produto_multiplicacao += int(digito) * multiplicador
            multiplicador -= 1
        
        valor_digito = (produto_multiplicacao * 10) % 11

        if valor_digito > 9:
            valor_digito = 0
            
        if str(valor_digito) == cpf.split('-')[1][digito_verificar]:
            pri_digit_verificado = True

            if cpf_valido:
                print('CPF VÁLIDO')
                break
            else:
                continue

        else:
            print('\033[31mCPF INVÁLIDO!\033[m')
            break


verificador_cpf('131.805.026-06')
    