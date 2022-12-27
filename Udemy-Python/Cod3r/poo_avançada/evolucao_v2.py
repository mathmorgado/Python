class Humano:
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
    
    def das_cavernas(self): # Método de instância (Só pode ser executado através da instância)
        self.especie = 'Homo Neanderthaliensis'
        return self

    # Método  estático
    @staticmethod
    def especies():  # Sem self (objeto da instância) como parâmetro!
        # Sem acesso aos methods/attrs de instância nem de classe (funcao 'normal')
        adjetivos = ('Habilis', 'Erectus', 'Neanderthaliensis', 'Sapiens')
        return ('Australopitecos',) + tuple(f'Homo {adj}' for adj in adjetivos)

    # Método de classe (pode ser acessado da própria classe) 
    @classmethod
    def is_evolucao(cls): # Ao invés de self recebe cls, já que aponta para a classe!
        # print(cls.__name__) Vai exibir o nome da classe referenciada
        return cls.especie == cls.especies()[-1]
    

class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

if __name__ == '__main__':
    mathias = HomoSapiens('Mathias')
    # HomoSapiens.das_cavernas(mathias)
    grog = Neanderthal('Grog')

    print(Humano.is_evolucao()) # Possivel de executar direto da classe (classmethod)  

    print(f'\nEvolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolução (a partir da instância): {", ".join(mathias.especies())}')

    print(f'\nHomo Sapiens é evoluído? {HomoSapiens.is_evolucao()}')
    print(f'Neanderthaliensis é evoluído? {Neanderthal.is_evolucao()}')

    print(f'\nMathias é evoluído? {mathias.is_evolucao()}')
    print(f'Grog é evoluído? {grog.is_evolucao()}')
