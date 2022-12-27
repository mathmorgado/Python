from Pacotes.Dados import Validacao as val
from Pacotes.UtilidadeCeV import Modulo_112 as mod

preco = val.LeiaDinheiro('Digite um valor: R$')
mod.resumo(preco, 50, 21)
