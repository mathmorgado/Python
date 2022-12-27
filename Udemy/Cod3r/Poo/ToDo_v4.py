from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    
    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))
    
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


def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Varrer quarto', datetime.now())
    casa.add('Lavar roupa')

    casa.procurar('Lavar roupa').concluir()

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