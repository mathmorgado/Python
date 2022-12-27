from Modulos import Modulo_107

preço = int(input('Digite um valor: R$'))
print(f'Aumentando o preço em 10%: R${Modulo_107.aumentar(preço)}')
print(f'Diminuindo o preço em 10%: R${Modulo_107.diminuir(preço)}')
print(f'O dobro do preço é: R${Modulo_107.dobro(preço)}')
print(f'A metade do preço é: R${Modulo_107.metade(preço)}')
