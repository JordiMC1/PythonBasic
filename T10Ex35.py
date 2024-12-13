def es_de_traspas():
    a = int(input("Posa un any i et diré si és de traspás o no: "))
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        print("L'any {} es de traspás.".format(a))
    else:
        print("L'any {} no és de traspás.".format(a))
es_de_traspas() 