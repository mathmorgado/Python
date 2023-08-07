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


comandos = {
    'listar': lambda: listar(tarefas),
    'desfazer': lambda: desfazer(tarefas, tarefas_desfeitas),
    'refazer': lambda: refazer(tarefas, tarefas_desfeitas),
    'adicionar': lambda: adicionar(task, tarefas),
    'clear': lambda: system('cls')
}

while True:
    print('\nComandos: Listar, Adicionar, Desfazer e Refazer')
    task = str(input('Digite a tarefa ou comando: ')).lower()

    comando = comandos.get(task) if comandos.get(task) is not None \
        else comandos['adicionar']

    comando()
