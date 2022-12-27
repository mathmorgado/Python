from app.negocio.backend import nomes

def nome_existe(nome):
    if nome in nomes:
        return True
    else:
        return False