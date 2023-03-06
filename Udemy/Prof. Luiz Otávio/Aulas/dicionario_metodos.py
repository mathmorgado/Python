"""
Métodos úteis dos dicionários em Python
1- len - quantas chaves
2- keys - iterável com as chaves
3- values - iterável com os valores
4- items - iterável com chaves e valores
5- setdefault - adiciona valor se a chave não existe
6- copy - retorna uma cópia rasa (shallow copy)
7- get - obtém uma chave
8- pop - Apaga um item com a chave especificada (del)
9- popitem - Apaga o último item adicionado
10-update - Atualiza um dicionário com outro
"""
import copy


pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900,
}

# Quantidade de items no dicionario
print(len(pessoa))

#.keys(), .values(), .items()
print(list(pessoa.keys())) # Retorna todas as chaves
print(list(pessoa.values())) # Retorna todos os valores
print(list(pessoa.items())) # Retorna todos os items (chave + valor)

# Usando for para retornar (values, keys or items)
for valor in pessoa.values():
    print(f'valores = {valor}')

for chave, valor in pessoa.items():
    print(f'Itens = {chave, valor}')

# Alterar algum valor 
pessoa.setdefault('idade', 18) # (900 -> 18)
print(pessoa['idade'])

# Copiar items de um dicionario para outro
pessoa2 = pessoa # Essa forma nn -copia- os items de 'Pessoa' para 'Pessoa2', mas indica que 'Pessoa2' aponta para o dicionario 'Pessoa'
pessoa2 = pessoa.copy() # Copia os items dentro de 'Pessoa' para 'Pessoa2' de forma "rasa" (sem copiar listas ou entrar em subnives)
pessoa2 = copy.deepcopy(pessoa) # Copia os items e todos os subnives dentro de 'Pessoa' para 'Pessoa2'

# pega uma chave se existir
if pessoa.get('nome') is None:
    print('Chave [nome] não existe!')

# pop x popitem
del_item_escolhido = pessoa.pop('idade')
del_ultimo_item = pessoa.popitem()

# Update - Atualiza/altera um dicionario
pessoa.update({
    'nome': 'Luiz O.',  # altera um valor já existente
    'sobrenome': 'Miranda', # Adiciona um novo valor
})

pessoa.update(nome='Luíz O.', idade=31)

print(pessoa)