tup = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',
       'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
       'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
num = int(input('Digite um número de 0 a 20 e irei o informar extenso: '))

while num > 20:
    print('\nResposta inválida!\n')
    num = int(input('Por favor digite um número entre 0 e 20: '))

print(f'{num} por escrito por extenso é: {tup[num]}')
