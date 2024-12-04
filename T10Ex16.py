def longitud():
    l = 1
    ll = input("introdueix una llista de paraules separades per comes: ")
    for i in ll:
        if i == ".":
            longitud += 1
    print(l)
longitud()