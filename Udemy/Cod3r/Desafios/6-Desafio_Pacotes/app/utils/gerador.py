from random import randint

def novo_nome():
    sil1 = ['Sa', 'Ma', 'Edu', 'Ra', 'An']
    sil2 = ['mu', 'te', 'ar', 'fa', 'der']
    sil3 = ['el', 'us', 'do', 'ela', 'son']

    nome = f'{sil1[randint(0, 4)]}{sil2[randint(0, 4)]}{sil3[randint(0, 4)]}'

    return nome
