# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
from os import system

tarefas = []
tarefas_desfeitas = []


def Menu(*Opções):
    print(30*'-')
    c = 1
    for opção in Opções:
        print(f'\033[93m{c}- \033[34m{opção}\033[m')
        c += 1
    print(30*'-')


Menu('Tarefas', 'Desfazer', 'Refazer', 'Clear')

while True:
    task = str(input('Digite a tarefa ou comando: ')).lower()

    if task == 'desfazer' or task == '2':

        try:

            if tarefas[-1] in tarefas_desfeitas:
                tarefas.pop()
            else:
                tarefas_desfeitas.append(tarefas.pop())
                print(tarefas_desfeitas)

        except IndexError:
            print('Nada para se desfazer')

    elif task == 'tarefas' or task == '1':
        print(tarefas)

    elif task == 'refazer' or task == '3':
        try:
            tarefas.append(tarefas_desfeitas.pop())
        except IndexError:
            print('Nada para se refazer')

    elif task == 'clear' or task == '4':
        system('cls')
        Menu('Tarefas', 'Desfazer', 'refazer', 'clear')

    else:
        if task in tarefas:
            continue
        else:
            tarefas.append(task)
