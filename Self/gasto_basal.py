from module_interface import linha, Menu
from os import system

taxa_ativ_dict = {'1': 1.2, '2': 1.375, '3': 1.55, '4': 1.725}

while True:
    Menu('Masculino', 'Feminino', title='Info')
    genero = int(input('Gênero biológico\033[32m[1/2]\033[m: '))

    if genero not in (1, 2):
        system('cls')
        print('\033[31mGênero inválido!\033[m\n')
        continue

    Menu('Sedentário', 'Pouco ativo',
         'Moderadamente ativo', 'Altamente ativo',
         title="Taxa de Atividade")

    taxa_ativ = str(input('Taxa de atividade\033[32m[1/2/3/4]\033[m: '))

    if taxa_ativ not in '1234':
        system('cls')
        print('\033[31mTaxa de atividade inválida!\033[m')
        continue

    linha()

    try:
        peso = float(input('\nPeso(kg): '))
        altura = float(input('Altura(cm): '))
        idade = int(input('Idade: '))
    except ValueError:
        system('cls')
        print('\033[31mError: Valor inválido!\033[m')
        continue

    break

imc = peso/((altura/100)**2)

if genero == 1:
    gasto_basal_masc = taxa_ativ_dict[taxa_ativ] * \
        (66+(13.7*peso)+(5*altura)-(6.8*idade))

    print(f'\nIMC: {imc:.1f}\nGasto basal: {gasto_basal_masc:.2f}Kcal')

else:
    gasto_basal_femin = taxa_ativ_dict[taxa_ativ] * \
        (655+(9.6*peso)+(1.8*altura)-(4.7*idade))

    print(f'\nIMC: {imc:.1f}\nGasto basal: {gasto_basal_femin:.2f}Kcal')
