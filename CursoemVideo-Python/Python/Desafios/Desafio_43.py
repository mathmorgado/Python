print('A seguir iremos calcular seu IMC (Indice de Massa Corporal) e '
      'informar se está abaixo do peso, acima ou no peso ideal.')

altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))
imc = peso / (altura * altura)

if imc < 18.50:
    print(f'Abaixo do peso! Seu IMC é {imc:.2f}.')
elif imc >= 18.50 and imc <= 25:
    print(f'Peso ideal! Seu IMC é {imc:.2f}.')
elif imc > 25 and imc <= 30:
    print(f'Sobrepeso! Seu IMC é {imc:.2f}.')
elif imc > 30 and imc <= 40:
    print(f'Obesidade! Seu IMC é {imc:.2f}!')
else:
    print(f'Obesidade mórbida! Seu IMC é {imc:.2f}!')
