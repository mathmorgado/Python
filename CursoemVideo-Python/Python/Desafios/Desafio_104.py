def LeiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\33[31mERROR! Digite um número inteiro válido')
        
        if ok:
            break
    return valor


m = LeiaInt('\33[39mDigite um número: ')
print(f'Você acabou de digitar o número {m}')