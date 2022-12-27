eleitores = int(input('Quantos eleitores tem em seu município? '))
voto_branco = int(input('Quantos desses eleitores votaram em branco? '))
voto_nulo = int(input('Quantos desses eleitores teve o voto anulado? '))
voto_valido = eleitores - voto_branco - voto_nulo

if voto_branco > eleitores:
    print('O numero de votos não pode ultrapassar o numero de eleitores!')
elif voto_nulo > eleitores:
    print('O numero de votos nulo não pode ultrapassar o numero de eleitores!')
else:
    percentual_votos = voto_valido/(eleitores/100)
    print(f'O percentual de votos do seu município é {percentual_votos:.0f}%!')
