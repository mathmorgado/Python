# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

alternativa = {'A': None, 'B': None, 'C': None, 'D': None}
acertos = 0

for c in range(0, len(perguntas)):
    print(f'\nQuestão {c+1}: {perguntas[c]["Pergunta"]}\n')
    cont = 0

    for chave in alternativa.keys():
        alternativa[chave] = perguntas[c]['Opções'][cont]
        cont += 1

    for k, v in alternativa.items():
        print(f'{k}) {v}')
        
    resposta = input('Escolha a alternativa: ').upper()

    if alternativa[resposta] == perguntas[c]['Resposta']:
        print('Acertou!')
        acertos += 1

    else:
        print('Errou!')
    
    print(f'\nVocê teve {acertos} acertos!')
    
