class Humano:
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    # Validar dado atraves do 'Get e Set'
    def get_idade(self):
        return self._idade
    
    def set_idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um numero positivo')
        self._idade = idade
    
    def das_cavernas(self):
        self.especie = 'Homo Neanderthaliensis'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthaliensis', 'Sapiens')
        return ('Australopitecos',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evolucao(cls):
        return cls.especie == cls.especies()[-1]
    

class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

if __name__ == '__main__':
    mathias = HomoSapiens('Mathias')
    mathias.set_idade(40)

    print(f'Nome: {mathias.nome} | Idade: {mathias.get_idade()}')

    grog = Neanderthal('Grog')
