print('A seguir iremos calcular o preço do produto de acordo'
      'com a condição de pagamento.')

produto = float(input('Qual o preço do produto? '))

print(' 1-À vista dinheiro/cheque.\n'
      ' 2-À vista no cartão.\n'
      ' 3-Em até 2x no cartão.\n'
      ' 4-3x ou mais no cartão.')

condicao = float(input('Qual a forma de pagamento? '))

if condicao == 1:
    preco = produto - (produto / 100 * 10)
    print(f'O preço do produto será de R${preco:.2f}')

elif condicao == 2:
    preco = produto - (produto / 100 * 5)
    print(f'O preço do produto será de R${preco:.2f}')

elif condicao == 3:
    preco = produto
    print(f'O preço do produto será R${preco:.2f}.'
          f'Com valor de R${preco / 2:.2f} à parcela')

else:
    parcela = int(input('Quantas parcelas? '))
    preco = produto + (produto / 100 * 20)
    parcelado = preco / parcela
    print(f'O preço do produto será de R${preco}!'
          f'Com valor de R${parcelado:.2f} à parcela')
