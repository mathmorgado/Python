def LeiaInt(valor):
    while True:
        try:
            entrada = int(input(valor))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Tipo de dado inválido! Por favor, digite um número inteiro.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar!\033[m')
            entrada = 0
            return entrada
        else:
            return int(entrada)


def LeiaFloat(valor):
    while True:
        try:
            entrada = float(input(valor))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Tipo de dado inválido! Por favor, digite um número inteiro.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário!\033[m')
            entrada = 0
            return entrada
        else:
            return float(entrada)