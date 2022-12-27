lista_1 = [2, 3, 4]
dobro = list(map(lambda x: x * 2, lista_1))

print(dobro)

lista_2 = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 27},
    {'nome': 'Carlinhos', 'idade': 48}
]

so_nomes = list(map(lambda lista: lista['nome'], lista_2))

print(so_nomes)

so_idade = map(lambda lista: lista['idade'], lista_2)

print(tuple(so_idade))

# Desafio: Usando map retorne frase '<Nome> tem <idade> anos.' Usando lista_2

clientes = map(lambda lista: f"{lista['nome']} tem {lista['idade']} anos.", lista_2)

print(list(clientes))
