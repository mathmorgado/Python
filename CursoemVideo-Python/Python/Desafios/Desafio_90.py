Cadastro = dict()
Qtde_alunos = int(input('Qtde de alunos à ser verificados: '))

for _ in range(0, Qtde_alunos):
    Cadastro['Nome'] = str(input('Nome: '))
    Cadastro['Media'] = float(input('Média: '))

    if Cadastro['Media'] < 6:
        Cadastro['Resultado'] = 'Reprovado!'
    else:
        Cadastro['Resultado'] = 'Aprovado!'

    for k, v in Cadastro.items():
        print(f'{k} é {v}', end=' | ')
    print('\n')
