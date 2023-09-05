def per_units():
    units = input("Units: ")
    qty_proteins = input("Amount of protein per unit: ")
    price = input("Price: ")

    try:
        qty_proteins = float(qty_proteins)
        price = float(price)
        units = int(units)
    except TypeError:
        print("Error: invalid values")

    price_protein = ((price / units) / qty_proteins)

    print(f"\nPrice per protein: R${price_protein:.2f}")


def per_gram():
    grams = input("Grams: ")
    price = input("Price: ")
    qty_proteins = input("Protein per 100g: ")

    try:
        qty_proteins = float(qty_proteins)
        price = float(price)
        grams = float(grams)
    except TypeError:
        print("Error: invalid values")

    price_protein = ((price / grams) / qty_proteins)

    print(f"\nPrice per protein: R${price_protein:.2f}")


def whey():
    grams = input("Total grams: ")
    price = input("Price: ")
    scoopy = input("Grams per scoopy: ")
    qty_proteins = input("Protein per scoopy: ")

    try:
        qty_proteins = float(qty_proteins)
        price = float(price)
        scoopy = float(scoopy)
        grams = float(grams)
    except TypeError:
        print("Error: invalid values")

    total_proteins = (qty_proteins * grams) / scoopy
    price_total_proteins = (total_proteins * price) / grams
    price_protein = (price_total_proteins / total_proteins)

    print(f"\nPrice per protein: R${price_protein:.2f}")
