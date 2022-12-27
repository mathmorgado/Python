def pig_it(strs):
    texto = strs.split()

    for i in range(0, len(texto)):
            texto[i] = texto[i][1:] + texto[i][0] + 'ay' if texto[i][0].isalpha() else texto[i]
    
    return ' '.join(texto)


print(pig_it('Pig latin is cool !'))
