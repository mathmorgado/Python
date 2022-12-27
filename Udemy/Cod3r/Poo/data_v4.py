class Data:
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano 


    def __str__(self):  # Modulo que já converte pra STR sem precisar ser chamado
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(29, 6, 2022)
print(f'\ndata 1: {d1}')

d1.dia = 17
d1.ano = 1967

print(f'\ndata 1(alterada): {d1}')

d2 = Data(ano=2025)
print(f'\ndata 2: {d2}\n')

