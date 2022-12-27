print('---CAIXA ELETRÔNICO---')
sacado = int(input('Valor a ser sacado: R$'))

cedula50 = sacado // 50
sacado -= cedula50 * 50

cedula20 = sacado // 20
sacado -= cedula20 * 20

cedula10 = sacado // 10
sacado -= cedula10 * 10

cedula1 = sacado // 1

print(f'Cédulas de R$50: {cedula50}\nCédulas de R$20: {cedula20}')
print(f'Cédulas de R$10: {cedula10}\nCédulas de R$1: {cedula1}')
