def suma_quadrats():
    num = int(input("Introdueix un número menor de 100: "))
    if num >= 100:
        print("El número ha de ser menor de 100.")
        return

    suma = 0
    for n in range(num - 4, 0, -4):
        suma += n ** 2

    print("La suma dels quadrats dels números són: {}".format(suma))
    
suma_quadrats()