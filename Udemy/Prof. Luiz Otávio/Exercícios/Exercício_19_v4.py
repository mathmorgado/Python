# Exercício - Lista de tarefas com desfazer e refazer SALVANDO JSON

from os import system
import json


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

    adicionar(tarefas_desfeitas.pop(), tarefas)


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'Udemy/Prof. Luiz Otávio/Exercícios/Exercício_19_v4.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_desfeitas = []

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
    salvar(tarefas, CAMINHO_ARQUIVO)
