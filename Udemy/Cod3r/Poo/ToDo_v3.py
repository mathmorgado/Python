from datetime import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    
    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))
    
    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]
    
    def procurar(self, descricao):
        # Possivel IndexError
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]
    
    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True
    
    def __str__(self):
        return self.descricao + (' (Concluída!)' if self.feito else '')


def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Varrer quarto')
    casa.add('Lavar roupa')

    casa.procurar('Lavar roupa').concluir()

    print(casa)
    for tarefa in casa:
        print(f'- {tarefa}')

    mercado = Projeto('Compras mercado')
    mercado.add('Tomate')
    mercado.add('Hambúrguer')
    mercado.add('Pão')
    
    comprar_hamburguer = mercado.procurar('Hambúrguer')
    comprar_hamburguer.concluir()

    print(mercado)
    for tarefa in mercado:
        print(f'- {tarefa}')


if __name__ == '__main__':
    main()