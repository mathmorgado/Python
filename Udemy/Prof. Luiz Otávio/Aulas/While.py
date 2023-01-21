"""
While / Else - Aula 8
Contadores
Acumuladores
"""

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

#   if contador == 8:
#       break

    acumulador += contador
    contador += 1
else:  # Se der um break, o else é ignorado 
    print('While tem else... Chocadah, Passadah :o')

print('Alegriaaaaa')

frase = 'O rato roeu a roupa do rei de roma'  # Interável
nova_string = ''
cont = 0

#  Interando <- Interar
while cont < len(frase):  # Deixar todos os R's maiúsculos!
    letra = frase[cont]

    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string += letra
    
    cont += 1
    print(nova_string)

print(nova_string)