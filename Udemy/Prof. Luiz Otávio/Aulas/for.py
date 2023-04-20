"""
Como o "For" funciona? 

O for é composto por 4 principais elementos:
1-Iterável -> str, range, etc (__iter__)
2-Iterador -> quem sabe entregar um valor por vez
3-next -> me entregue o próximo valor
4-iter -> me entregue seu iterador

Observe o seguinte 'for':
  for letra in texto:
      print(letra)

O 1º elemento é a variavél 'texto, já o 2º, 3º e 4º elementos são, juntos, a variável 'letra'.
Para melhor entendimento, observe o exemplo abaixo:
"""

# Exemplo de como funciona o 'for' mostrado acima
texto = 'Luiz'  # iterável
iteratador = iter(texto)  # iterador/iter

while True: # Repetição do processo
    try:
        letra = next(iteratador) # Variavel onde armazena o valor interado pelo iterador e next
        print(letra)
    except StopIteration: # Erro de interation quando tenta buscar um proximo valor que nn existe
        break

