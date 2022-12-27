from datetime import datetime

ano_nasc = int(input('Em que ano voce nasceu? '))
mes_nasc = int(input('De qual mês? '))

mes_hoje = int(datetime.today().strftime('%m'))
ano_hoje = int(datetime.today().strftime('%Y'))

if ano_hoje <= (ano_nasc + 9):
    print('Você é um nadador mirim!')

elif ano_hoje >= (ano_nasc + 9) and ano_hoje < (ano_nasc + 14):
    if mes_hoje >= mes_nasc:
        print('Você é um nadador infantil!')
    else:
        falta = mes_nasc - mes_hoje
        print(f'Faltam {falta} meses para você ser um infantil!')

elif ano_hoje >= (ano_nasc + 14) and ano_hoje <= (ano_nasc + 18):
    if mes_hoje >= mes_nasc:
        print('Você é um nadador junior!')
    else:
        falta = mes_nasc - mes_hoje
        print(f'Faltam {falta} meses para você ser um junior!')

elif ano_hoje >= (ano_nasc + 19) and ano_hoje <= (ano_nasc + 20):
    if mes_hoje >= mes_nasc:
        print('Você é um nadador sênior!')
    else:
        falta = mes_nasc - mes_hoje
        print(f'Faltam {falta} meses para você ser um sênior!')

elif ano_hoje > (ano_nasc + 20):
    if mes_hoje >= mes_nasc:
        print('Você é um nadador master!')
    else:
        falta = mes_nasc - mes_hoje
        print(f'Faltam {falta} meses para você ser um master!')
