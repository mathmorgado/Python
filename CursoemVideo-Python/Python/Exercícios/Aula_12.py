# Estrutura de controle aninhada
nome = str(input('Qual é o seu nome? ')).strip()

if nome.lower() == 'matheus':
    print('Que nome sensual ein, seu goxtosão!')
elif nome.lower() == 'vitoria':
    print('Oi more de mi vida, vem sempre aqui?')
elif nome in 'Pedro Debora Felipe':
    print('Qual é parça, c é fera ein!')
else:
    print('Que nome bosta...')

print(f'Tenha um bom dia, {nome}!')
