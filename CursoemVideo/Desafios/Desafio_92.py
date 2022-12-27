from datetime import date
data_atual = date.today()

cadastro = {}
cadastro['Nome'] = str(input('Nome: '))
cadastro['Nascimento'] = int(input('Ano de Nascimento: '))
cadastro['Carteira'] = int(input('Carteira de trabalho(0 se não tem): '))
cadastro['Idade'] = int(data_atual.year) - cadastro['Nascimento']

if cadastro['Carteira'] > 0:
    cadastro['Ano_contratacao'] = int(input('Ano de contratação: '))
    cadastro['Salario'] = int(input('Salário: '))
    cadastro['Aposentadoria'] = cadastro['Ano_contratacao'] + 35
print('\nSUAS INFORMAÇÕES:         ')
for k, v in cadastro.items():
    print(f' |{k}: {v}')
