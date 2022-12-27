from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    # Sobrecarga do operador +=
    # projeto += tarefa
    # casa += ...
    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)
    
    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))
    
    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)
    
    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]
    
    def procurar(self, descricao):
        # Possivel IndexError
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]
    
    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True
    
    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluida)')
        elif self.vencimento:
            if self.vencimento < datetime.now():
                status.append('(vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')
        
        return f'{self.descricao} ' + ' '.join(status)


class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias
        self.dono = None

    def concluir(self):
        super().concluir()
        novo_vencimeto = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(self.descricao, novo_vencimeto, self.dias)
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa


def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Varrer quarto', datetime.now())
    casa.add('Lavar roupa')

    casa.procurar('Lavar roupa').concluir()

    casa += TarefaRecorrente('Trocar lençol', datetime.now(), dias=10)
    casa.procurar('Trocar lençol').concluir()

    print(casa)
    for tarefa in casa:
        print(f'- {tarefa}')

    mercado = Projeto('Compras mercado')
    mercado.add('Tomate')
    mercado.add('Hambúrguer')
    mercado.add('Pão', datetime.now() + timedelta(days=3, seconds=1))
    
    comprar_hamburguer = mercado.procurar('Hambúrguer')
    comprar_hamburguer.concluir()

    print(mercado)
    for tarefa in mercado:
        print(f'- {tarefa}')


if __name__ == '__main__':
    main()