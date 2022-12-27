from datetime import datetime

ano_hoje = int(datetime.today().strftime('%Y'))

dic = {}

for c in range(0, 7):
    nome = input('Qual seu nome? ')
    ano_nasc = int(input('Em qual ano você nasceu? '))
    dic[nome] = ano_nasc
    if ano_hoje <= (ano_nasc + 21):
        print('Você não alcançou a maioridade!')
    else:
        print('Você alcançou a maioridade!')
