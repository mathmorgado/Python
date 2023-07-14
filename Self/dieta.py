from module_interface import linha, Menu

taxa_ativ_dict = {'1': 1.2, '2': 1.375, '3': 1.55, '4': 1.725}

while True:
    Menu('Masculino', 'Feminino', title='Info')
    genero = int(input('Gênero biológico[1/2]: '))

    if genero not in (1, 2):
        print('Gênero inválido!')
        continue

    linha()

    print('1- Sedentário\n2- Pouco ativo\n'
          '3- Moderadamente ativo\n4- Altamente ativo')
    taxa_ativ = str(input('Taxa de atividade[1/2/3/4]: '))

    if taxa_ativ not in '1234':
        print('Taxa de atividade inválida!')
        continue

    linha()

    break


peso = float(input('Peso(kg): '))
altura = float(input('Altura(cm): '))
idade = int(input('Idade: '))

imc = peso/(altura**2)

gasto_basal_masc = taxa_ativ_dict[taxa_ativ] * \
    (66+(13.7*peso)+(5*altura)-(6.8*idade))

gasto_basal_femin = taxa_ativ_dict[taxa_ativ] * \
    (655+(9.6*peso)+(1.8*altura)-(4.7*idade))

print(f'IMC: {imc:.1f}\nGasto basal: {gasto_basal_masc:.2f}Kcal')
