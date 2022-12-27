from Modulos import Modulo_108 as mod

preço = int(input('Digite um valor: R$'))
print(f'Aumentando o preço em 10%: R${mod.moeda(mod.aumentar(preço))}')
print(f'Diminuindo o preço em 10%: R${mod.moeda(mod.diminuir(preço))}')
print(f'O dobro do preço é: R${mod.moeda(mod.dobro(preço))}')
print(f'A metade do preço é: R${mod.moeda(mod.metade(preço))}')
