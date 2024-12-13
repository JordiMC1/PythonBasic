def calcular_capital_final():

    capital_inicial = float(input("Introdueix la quantitat inicial (50000€ - 800000€): "))
    if not (50000 <= capital_inicial <= 800000):
        print("La quantitat inicial ha d'estar entre 50000€ i 800000€.")
        return

    interes = float(input("Introdueix l'interès (0.5 per cent - 13 per cent): "))
    if not (0.5 <= interes <= 13):
        print("L'interès ha d'estar entre 0.5 i 13.")
        return

    anys = int(input("Introdueix el nombre d'anys (3 - 40): "))
    if not (3 <= anys <= 40):
        print("El nombre d'anys ha d'estar entre 3 i 40.")
        return

    capital_final = capital_inicial * (1 + interes / 100) ** anys

    print("El capital final després de {} anys és: {}€".format(anys, capital_final))

calcular_capital_final() 