from .compras import *
from datetime import datetime


def get_data(compra):
    return compra.data



class Pessoas:
    def __init__(self, nome, idade):
        self.idade = idade
        self.nome = nome

    def __str__(self):
        return f'Cliente: {self.nome} - {self.idade} anos'

    def is_Adult(self):
        if self.idade:
            if self.idade >= 18:
                return True
            else:
                return False
        else:
            return False


class Cliente(Pessoas):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []
    
    def registrar_compra(self, compra):
        self.compras.append(compra)
    
    def get_data_ultima_compra(self):
        return None if not self.compras else sorted(self.compras, key=get_data)[-1].data

    def total_compras(self):
        total = 0
        for compra in self.compras:
            total += compra.valor
        return total


class Vendedor(Pessoas):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
