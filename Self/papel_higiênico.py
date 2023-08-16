qtde_rolo = float(input("Qtde rolo: "))
metros_rolo = float(input("Metro por rolo: "))
preco = float(input("Preço: "))

metros_total = metros_rolo * qtde_rolo
preco_metro = preco / metros_total

print(f"\nPreco por metro: R${preco_metro:.3f}")
