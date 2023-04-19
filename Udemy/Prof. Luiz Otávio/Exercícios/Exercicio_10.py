frase = 'O Rato roeu a roupa do Rei de roma, mas o rei de roma não roeu a roupa do rato'

i = 0
while i < len(frase):
    letra = frase.lower()[i]
    letra_mais_aperecida = None
    qtde_letra = 0

    if i == 0:
        letra_mais_aperecida = letra
        qtde_letra = frase.lower().count(letra)
        i += 1
        continue
    
    if letra == ' ':
        i += 1
        continue
    
    if frase.lower().count(letra) > qtde_letra:
        letra_mais_aperecida = letra
        qtde_letra = frase.lower().count(letra)

    i += 1

print(f'A letra mais aparecida foi "{letra_mais_aperecida.upper()}", tendo aparecido {qtde_letra} vezes!')

