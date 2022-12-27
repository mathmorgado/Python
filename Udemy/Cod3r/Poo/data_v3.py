class Data:
    def __str__(self):  # Modulo que já converte pra STR sem precisar ser chamado
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
d1.dia = 29
d1.mes = 6
d1.ano = 2022

print(d1)

d2 = Data()
d2.dia = 29
d2.mes = 11
d2.ano = 2022

print(d2)
