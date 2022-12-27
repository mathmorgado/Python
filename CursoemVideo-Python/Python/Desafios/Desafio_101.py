from datetime import date
hoje = date.today()


def voto(nascimento):
    global idade
    idade = int(hoje.strftime("%Y")) - nascimento
    if idade < 16:
        return 'VOTO NEGADO'
    elif idade >= 16 and idade < 18:
        return 'VOTO OPCIONAL'
    elif idade >= 18 and idade < 65:
        return 'VOTO OBRIGATÓRIO'
    elif idade >= 65 and idade < 200:
        return 'VOTO OPCIONAL'
    else:
        return 'A idade escolhida não existe!'


data_nascimento = int(input('Data de nascimento: '))
eleitor = voto(data_nascimento)

print(f'Com {idade} anos: {eleitor}')
