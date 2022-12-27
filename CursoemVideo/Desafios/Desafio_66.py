s = 0
while True:
    numb = int(input('Digite um número inteiro: '))
    if numb == 999:
        break
    s += numb

print(f'A soma dos numeros digitados é: {s}')
