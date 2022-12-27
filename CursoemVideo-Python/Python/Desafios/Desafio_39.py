from datetime import datetime

dia_nasc = int(input('Qual o dia do seu nascimento? '))
mes_nasc = int(input('Qual o mes do seu nascimento? '))
ano_nasc = int(input('Qual o ano do seu nascimento? '))

dia_hoje = int(datetime.today().strftime('%d'))
mes_hoje = int(datetime.today().strftime('%m'))
ano_hoje = int(datetime.today().strftime('%Y'))

if ano_hoje < ano_nasc + 18:
    falta = (ano_nasc + 18) - ano_hoje
    print(f'Ainda não está na hora do alistamento! Falta(m) {falta} ano(s)')

elif ano_hoje == (ano_nasc + 18):

    if mes_hoje >= mes_nasc:
        print('Já está na hora de fazer o alistameno militar!')
    else:
        print('Está quase na hora de fazer o alistamento militar! Falta pouco')

else:
    print('Já passou a hora de fazer o alistamento militar!')
