def multiplicacao(multiplicador):
    def multiplicando(fator):
        return fator * multiplicador
    return multiplicando


Dobro = multiplicacao(2)
triplo = multiplicacao(3)
quadruplo = multiplicacao(4)

print(Dobro(10))
print(triplo(10))
print(quadruplo(10))