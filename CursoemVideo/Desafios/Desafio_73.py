tup = ('Flamengo', 'Palmeiras', 'Atlético Mineiro', 'Grêmio',
       'Athletico Paranaense', 'Santos', 'São Paulo', 'Internacional',
       'Fluminense', 'Corinthians', 'Fortaleza', 'Bahia', 'Ceará',
       'Cruzeiro', 'América Mineiro', 'Atlético Goianiense',
       'Chapecoense', 'Botafogo', 'Vasco da Gama', 'Red Bull Bragantino')

pos_chap = tup.index('Chapecoense')

print(f'A) Os 5 primeiros são: {tup[0:5]}')
print(f'B) Os 4 ultimos são: {tup[-4:]}')
print(f'C)Ordem alfabética dos times: {sorted(tup)}')
print(f'D) A Chapecoense está em: {pos_chap + 1}')
