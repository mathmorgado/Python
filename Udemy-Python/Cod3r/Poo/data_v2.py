class Data:
    def to_str(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
d1.dia = 29
d1.mes = 6
d1.ano = 2022

print(d1.to_str())

d2 = Data()
d2.dia = 29
d2.mes = 11
d2.ano = 2022

print(d2.to_str())
