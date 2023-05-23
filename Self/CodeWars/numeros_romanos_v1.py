"""
Dados importantes: Parâmetro entre 1 e 3999 / 1000 -> M, 500 -> 100 -> C, 50 -> L, 10 -> X / 900 -> CM, 90 -> XC, 9 -> IX.

Lógica:
-Tratamento de erros
-
-
-
-
-
-
"""

def conversor_romano(num):

    if str(num).isnumeric() and int(num) <= 3999 and int(num) > 0:
        num = str(num)
        
        if int(num) >= 1000:
            milhar = (int(num[0])*'M')

            # Casa Centenas

            if int(num[1]) < 4:
                centena = (int(num[1])*'C')

            elif int(num[1]) == 4:
                centena = 'CD'
            
            elif int(num[1]) == 5:
                centena = 'D'

            elif int(num[1]) > 5 and int(num[1]) < 9:
                centena = ('D'+(int(num[1])-5)*'C')
            
            else:
                centena = 'CM'

            # Casa Dezenas

            if int(num[2]) < 4:
                dezena = (int(num[2])*'X')
            
            elif int(num[2]) == 4:
                dezena = 'XL'
            
            elif int(num[2]) == 5:
                dezena = 'L'

            elif int(num[2]) > 5 and int(num[2]) < 9:
                dezena = ('L'+(int(num[2])-5)*'X')
            
            else:
                dezena = 'XC'
            
            # Casa Unidades

            if int(num[3]) < 4:
                unidade = (int(num[3])*'I')
            
            elif int(num[3]) == 4:
                unidade = 'IV'
            
            elif int(num[3]) == 5:
                unidade = 'V'

            elif int(num[3]) > 5 and int(num[3]) < 9:
                unidade = ('V'+(int(num[3])-5)*'I')
            
            else:
                unidade = 'IX'
                
            return milhar + centena + dezena + unidade


        elif int(num) >= 100:

            if int(num[0]) < 4:
                centena = (int(num[0])*'C')

            elif int(num[0]) == 4:
                centena = 'CD'
            
            elif int(num[0]) == 5:
                centena = 'D'

            elif int(num[0]) > 5 and int(num[0]) < 9:
                centena = ('D'+(int(num[0])-5)*'C')
            
            else:
                centena = 'CM'
            
            # Casa Dezenas

            if int(num[1]) < 4:
                dezena = (int(num[1])*'X')
            
            elif int(num[1]) == 4:
                dezena = 'XL'
            
            elif int(num[1]) == 5:
                dezena = 'L'

            elif int(num[1]) > 5 and int(num[1]) < 9:
                dezena = ('L'+(int(num[1])-5)*'X')
            
            else:
                dezena = 'XC'
            
            # Casa Unidades

            if int(num[2]) < 4:
                unidade = (int(num[2])*'I')
            
            elif int(num[2]) == 4:
                unidade = 'IV'
            
            elif int(num[2]) == 5:
                unidade = 'V'

            elif int(num[2]) > 5 and int(num[2]) < 9:
                unidade = ('V'+(int(num[2])-5)*'I')
            
            else:
                unidade = 'IX'
            
            return centena + dezena + unidade

        elif int(num) >=10:

            if int(num[0]) < 4:
                dezena = (int(num[0])*'X')
            
            elif int(num[0]) == 4:
                dezena = 'XL'
            
            elif int(num[0]) == 5:
                dezena = 'L'

            elif int(num[0]) > 5 and int(num[0]) < 9:
                dezena = ('L'+(int(num[0])-5)*'X')
            
            else:
                dezena = 'XC'
            
            # Casa Unidades

            if int(num[1]) < 4:
                unidade = (int(num[1])*'I')
            
            elif int(num[1]) == 4:
                unidade = 'IV'
            
            elif int(num[1]) == 5:
                unidade = 'V'

            elif int(num[1]) > 5 and int(num[1]) < 9:
                unidade = ('V'+(int(num[1])-5)*'I')
            
            else:
                unidade = 'IX'

            return dezena + unidade

        else:

            if int(num[0]) < 4:
                unidade = (int(num[0])*'I')
            
            elif int(num[0]) == 4:
                unidade = 'IV'
            
            elif int(num[0]) == 5:
                unidade = 'V'

            elif int(num[0]) > 5 and int(num[0]) < 9:
                unidade = ('V'+(int(num[0])-5)*'I')
            
            else:
                unidade = 'IX'


            return unidade

    else:
        print('\033[31m Número inválido! \033[m')

        
teste = 367
print(conversor_romano(teste))