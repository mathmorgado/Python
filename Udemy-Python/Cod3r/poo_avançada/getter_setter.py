
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual /100))
    
    # Getter
    @property
    def nome(self):
        return self._nome
    
    # Setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor.replace('a', '@')
    
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        
        self._preco = valor

if __name__ == '__main__':
    p1 = Produto('Camiseta', 'R$50')
    p1.desconto(10)
    print(p1.nome, p1.preco)

    p2 = Produto('Controle', 200)
    p2.desconto(33)
    print(p2.nome, p2.preco)
