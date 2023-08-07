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


def listar(tarefas):
    if not tarefas:
        print('\nNão tem nehuma tarefa na lista!')
        return

    print('\nTarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')


def adicionar(tarefa, tarefas):
    if not tarefa:
        print('\nNenhuma tarefa digitada!')
        return

    tarefas.append(tarefa) if tarefa not in tarefas else None


def desfazer(tarefas, tarefas_desfeitas):
    if not tarefas:
        print('\nNenhuma tarefa para desfazer!')
        return

    tarefas_desfeitas.append(tarefas.pop()) if tarefas[-1] \
        not in tarefas_desfeitas else tarefas.pop()


def refazer(tarefas, tarefas_desfeitas):
    if not tarefas_desfeitas:
        print('\nNenhuma tarefa para refazer!')
        return

    tarefas.append(tarefas_desfeitas.pop())


Menu('Listar', 'Desfazer', 'Refazer', 'Clear')

while True:
    task = str(input('\nDigite a tarefa ou comando: ')).lower()

    if task == 'desfazer' or task == '2':
        desfazer(tarefas, tarefas_desfeitas)

    elif task == 'listar' or task == '1':
        listar(tarefas)

    elif task == 'refazer' or task == '3':
        refazer(tarefas, tarefas_desfeitas)

    elif task == 'clear' or task == '4':
        system('cls')
        Menu('Tarefas', 'Desfazer', 'refazer', 'clear')

    else:
        adicionar(task, tarefas)
