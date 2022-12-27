from time import time


# Define nosso decorator
def calcula_duracao(funcao):
    def wrapper():
        # Calcula o tempo de execução
        tempo_inicial = time()
        funcao()
        tempo_final = time()

        # Formata a mensagem que será mostrada na tela
        print(f'[{funcao.__name__}] Tempo total de execução: {str(tempo_final - tempo_inicial)}')
    
    return wrapper


# Decora a função com o decorator
@calcula_duracao
def main():
    for c in range(0, 10000000):
        pass

if __name__ == '__main__':
    main()
