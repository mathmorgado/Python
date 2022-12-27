num = int(input('Digite um número inteiro: '))
num1 = num
fatorial = num

while num != 1:
    num -= 1
    fatorial *= num

print(f'{num1}! = {fatorial} ')
