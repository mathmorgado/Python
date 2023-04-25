"""
Exercício - Lista de Compras

[x] Criar menu de opções com: Inserir, Apagar e Listar
[x] Construir a funcionalidade das opções
[x] Exibir o índice e o valor da lista
[x] Tratar erros
"""

lista_compras = []

while True:
    opcao = str(input('\nSelecione uma opção\n[i]nserir [a]pagar [l]istar [s]air: ')).lower().strip()
    
    if opcao == 'i':
        item = str(input('Item que deseja inserir: '))
        lista_compras.append(item)
    
    elif opcao == 'a':
        try:
            item = int(input('índice do item que deseja apagar: '))
            lista_compras.pop(item)
        except:
            print('\n\033[31mError: Opção inválida!\033[m\n')
            continue
    
    elif opcao == 'l':
        print()

        print(32*'~')
        print('LISTA DE COMPRAS'.center(32))
        print(32*'~')

        for indice, item in enumerate(lista_compras):
            print(indice, item)

        print()
    
    elif opcao == 's':
        print('SAINDO...')
        break

    else:
        print('\n\033[31mError: Opção inválida!\033[m\n')
        continue
