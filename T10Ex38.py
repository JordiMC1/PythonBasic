def paraules_que_rimen():
    a = input("Posa la primera paraula que vols que rimi: ")
    b = input("Posa la segona paraula que vols que rimi: ")
    if a [-3] == b[-3]:
        print("Les paraules {} i {} rimen les seves ultimes 3 lletres.".format(a,b))
    elif a [-2] == b[-2]:
        print("Les paraules {} i {} rimen les seves ultimes 2 lletres.".format(a,b))
    else:
        print("Les paraules {} i {} no rimen ninguna lletra.".format(a,b))

paraules_que_rimen()