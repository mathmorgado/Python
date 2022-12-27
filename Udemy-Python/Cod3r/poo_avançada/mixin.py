class HtmlToStringMixin:
    def __str__(self):
        # Conversão para Html
        html = super().__str__().replace('(', '<strong>(').replace(')', ')</strong>')
        return f'<span>{html}</span>'


class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return self.nome


class Animal:
    def __init__(self, nome, pet=True) -> None:
        self.nome = nome
        self.pet = pet

    def __str__(self) -> str:
        return self.nome + '(pet)' if self.pet else ''


class PessoaHtml(HtmlToStringMixin, Pessoa):
    pass


class AnimalHtml(HtmlToStringMixin, Animal):
    pass


if __name__ == '__main__':
    p1 = Pessoa('Marcos')
    print(p1)

    p2 = PessoaHtml('Marcaoo')
    print(p2)

    toto1 = Animal('Dengo')
    print(toto1)

    toto2 = AnimalHtml('Toto')
    print(toto2)