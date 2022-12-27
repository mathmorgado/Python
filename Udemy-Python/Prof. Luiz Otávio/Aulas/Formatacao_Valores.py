"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NUMERO)f - Quantidade de casas decimais (float)
:(CARACTERE) (> OU < OU ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

n = 'TTT'
print(f'{n:0^15}')
print(f'{n:n<15}')
print(f'{n:>15}')

num = 33 / 8
print(f'PADRÃO: {num}')
print(f'{num:.2f}')