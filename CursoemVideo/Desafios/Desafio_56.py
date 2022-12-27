maioridadehomem = 0
nomevelho = ''
media = []
totmulher20 = 0

for c in range(1, 5):
    print(f'---- {c}º PESSOA ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    media.append(idade)
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

print(f'A média de idade é: {sum(media) / 4}.')
print(f'O nome do homem mais velho é {nomevelho}, com {maioridadehomem} anos.')
print(f'O número de mulheres com menos de 20 anos é {totmulher20}.')
