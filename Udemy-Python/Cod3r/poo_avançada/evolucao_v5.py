class Humano:
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @property
    def idade(self):
        return self._idade
    
    # Propriedade abstrata (não implementada)
    @property
    def inteligente(self):
        raise NotImplementedError('Propriedade não implementada')
    
    @idade.setter
    def idade(self, idade):
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

    # Propriedade concreta
    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    # Propriedade concreta
    @property
    def inteligente(self):
        return True

if __name__ == '__main__':
    anonimo = Humano('Stuart')
    
    try:
        print(anonimo.inteligente)
    except NotImplementedError:
        print('Propriedade abstrata')

    greg = Neanderthal('Greg')
    jose = HomoSapiens('José')
    print(f'{jose.nome} da classe {jose.__class__.__name__}, inteligente: {jose.inteligente}')
    print(f'{greg.nome} da classe {greg.__class__.__name__}, inteligente: {greg.inteligente}')
