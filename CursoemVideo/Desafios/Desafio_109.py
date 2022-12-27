from Modulos import Modulo_109 as mod

preço = int(input('Digite um valor: R$'))
print(f'Aumentando o preço em 10%: R${mod.aumentar(preço, format=True)}')
print(f'Diminuindo o preço em 10%: R${mod.diminuir(preço, format=True)}')
print(f'O dobro do preço é: R${mod.dobro(preço, format=True)}')
print(f'A metade do preço é: R${mod.metade(preço, format=True)}')
