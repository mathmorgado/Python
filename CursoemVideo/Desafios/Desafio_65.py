n = int(input('Digite um valor: '))
resp = str(input('\nDeseja continuar? '))
maior = menor = n
lista = [n]

while resp.upper() == 'SIM':
    n = int(input('\nDigite outro valor: '))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    lista.append(n)
    resp = str(input('Deseja continuar? ')).strip()

print(f'A média dos números escolhidos é : {sum(lista) / len(lista):.2f}')
print(f'Maior valor escolhido: {maior}\nMenor valor escolhido: {menor}')
