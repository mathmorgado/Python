# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')

s1 = set()  # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

s2 = set()
s2.add('Matheus')
s2.update(('Valor já interado',))

print(s2)

s2.discard('Matheus')
print(s2)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

conjunto1 = {1, 2, 3}
conjunto2 = {2, 3, 4}
conjunto3 = set()

conjunto3 = conjunto1 | conjunto2
conjunto3 = conjunto1 & conjunto2
conjunto3 = conjunto1 - conjunto2 # A ordem importa mostra apenas o da esquerda
conjunto3 = conjunto1 ^ conjunto2 # Ordem nn importa, mostra ambas as diferenças

print(conjunto3)