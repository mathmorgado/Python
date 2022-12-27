from datetime import datetime
from desafio_loja import Cliente, Vendedor, Compra

def main():
    cliente = Cliente('Matheus Morgado', 25)
    vendedor = Vendedor('Pedro Henrique', 24, 1100)
    compra1 = Compra(cliente, datetime.now(), 150)
    compra2 = Compra(cliente, datetime(2022, 9, 7), 222)

    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)

    print(f'Cliente: {cliente}' '(adulto)' if cliente.is_Adult() else '')
    print(f'Vendedor: {vendedor}')

    valor_total = cliente.total_compras()
    qtde_compras = len(cliente.compras)

    print(f'Total: {valor_total} em {qtde_compras} compras.')
    print(f'Última compra: {cliente.get_data_ultima_compra()}')



if __name__ == '__main__':
    main()
