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
import re

def verificador_cpf(cpf, retornar_ultimos_digitos=False):
    pri_digit_verificado = False
    digitos_cpf = re.sub(r'[^0-9]', '', cpf)
    entrada_sequencial = digitos_cpf == digitos_cpf[0] * len(digitos_cpf)
    ultimos_digitos = '-'

    if len(cpf) > 14:
        return False
        
    if entrada_sequencial:
        print('\033[31mVocê enviou dados sequencias\033[m')
        return False

    while True:
        if pri_digit_verificado:
            digito_verificar = -1
            produto_multiplicacao = 0
            multiplicador = 11
            cpf_valido = True
        else:
            digito_verificar = -2
            produto_multiplicacao = 0
            multiplicador = 10
            cpf_valido = False

        for digito in digitos_cpf[0:9]:
            produto_multiplicacao += int(digito) * multiplicador
            multiplicador -= 1
        
        valor_digito = (produto_multiplicacao * 10) % 11

        if valor_digito > 9:
            valor_digito = 0

        if retornar_ultimos_digitos == True:
                digitos_cpf += str(valor_digito)
                digito_verificar = -1
            
        if str(valor_digito) == digitos_cpf[digito_verificar]:
            pri_digit_verificado = True
            ultimos_digitos += str(valor_digito)

            if cpf_valido:
                if retornar_ultimos_digitos == True:
                    return ultimos_digitos
                else:
                    return True
            else:
                continue

        else:
            return False


# print(verificador_cpf('340435095-22'))