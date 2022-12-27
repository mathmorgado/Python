genero = str(input('Qual seu gênero sexual[F/M]? '))

while genero.upper() not in 'FM':
    genero = str(input('Resposta inválida! Qual seu gênero sexual?[F/M] '))

print('FIM')
