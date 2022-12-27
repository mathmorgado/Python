def Notass(*Notas, Sit=False):
    """
    -> Função de análise das notas de diversos alunos:
    :param Notas: Uma nota ou mais do aluno.
    :param Sit: Indica se deve ou não informar a situação.
    :return: Retorna um dicionário com várias informações do aluno.
    """
    Nota = {}
    Nota['Total'] = len(Notas)
    Nota['Notas'] = sorted(Notas)
    Nota['Maior'] = Nota['Notas'][-1]
    Nota['Menor'] = Nota['Notas'][0]
    Nota['Média'] = sum(Nota['Notas']) / Nota['Total']
    if Sit == True:
        if Nota['Média'] >= 7:
            Nota['Situação'] = 'Boa!'
        else:
            Nota['Situação'] = 'Ruim!'
    return Nota


print(Notass(5.5, 3.5, 10, 8.5, 7.5, Sit=True))
help(Notass)

