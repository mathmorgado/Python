class Humano:
    # Membro de classe (estático)
    especie = 'Homo Sapiens' # Atributo de classe (Igual em todas as instâncias e pode ser acessado pela classe)

    def __init__(self, nome):
        self.nome = nome # Atributo de instância (Pode variar de instância à instãncia e não pode ser acessado pela classe)
    
    def das_cavernas(self):
        self.especie = 'Homo Neanderthaliensis'
        return self


if __name__ == '__main__':
    mathias = Humano('Mathias')
    grog = Humano('Grog').das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'mathias.especie {mathias.especie}')
    print(f'grog.especie: {grog.especie}')
